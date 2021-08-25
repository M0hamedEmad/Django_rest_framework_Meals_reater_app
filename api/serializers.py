from rest_framework import serializers
from .models import Meal, Rating

class MealSerializer(serializers.ModelSerializer):
    average_rate = serializers.SerializerMethodField()
    total_rating = serializers.SerializerMethodField()

    class Meta:
        model = Meal
        fields = ['id', 'title', 'description', 'average_rate', 'total_rating']

    def get_average_rate(self, obj):
        ratings = Rating.objects.filter(meal=obj)
        if ratings:
            return sum(rate.stars for rate in ratings) / len(ratings)
        return 0

    def get_total_rating(self, obj):
        ratings = Rating.objects.filter(meal=obj)
        return len(ratings)


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['stars', 'user', 'meal']