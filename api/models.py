from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class User(AbstractUser):
    pass

class DishType(models.Model):
    dish_type = models.CharField(max_length=50)

class Recipe(models.Model):
    recipe_text = models.CharField(max_length=300)

class Ingredients(models.Model):
    ingredient = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    units = models.CharField(max_length=50)



class Dish(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    dish_difficulty = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    dish_type = models.ManyToManyField(DishType)
    recipes = models.ManyToManyField(Recipe)
    ingredients = models.ManyToManyField(Ingredients)

class Image(models.Model):
    dish = models.PositiveIntegerField()
    image = models.ImageField(upload_to='api/files/cover')