from django.contrib import admin
from .models import Meal, Rating

class MealAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_filter = ['id', 'title', 'description']
    search_fields = ['title', 'description']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'meal', 'stars']
    list_filter = ['user', 'meal', 'stars']


admin.site.register(Meal, MealAdmin)
admin.site.register(Rating, RatingAdmin)
