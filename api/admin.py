from django.contrib import admin
from .models import User, Dish, Recipe, Ingredients, DishType, Image
# Register your models here.

admin.site.register(User)
admin.site.register(Dish)   
admin.site.register(Recipe)
admin.site.register(Ingredients)
admin.site.register(DishType)
admin.site.register(Image)