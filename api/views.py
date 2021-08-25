from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from .serializers import MealSerializer, RatingSerializer
from .models import Meal, Rating

class MealViewSet(ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(detail=True, methods=['post'])
    def rate_meal(self, requet, pk=None):
        if 'stars' in requet.data:
            meal = Meal.objects.get(id=pk)
            user = requet.data['user']
            stars = requet.data.get('stars')
            try:
                # Upadte rateing
                rating = Rating.objects.get(meal=meal, user=user)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating)
                json = {
                    "message": "Meal rateing updated",
                    "result": serializer.data
                }
                return Response(json)

            except Rating.DoesNotExist:
                # Create new rate
                rating = Rating.objects.create(stars=stars, meal=meal, user=user)
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'Meal Rate Created',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_200_OK)

        return Response(
            {"message":"stars not provided"},
             status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer