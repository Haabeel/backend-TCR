import json
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import User, Dish, Recipe, DishType, Ingredients, Image

class CustomRegisterSerializer(RegisterSerializer):
    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self._validated_data.get('username', ''),
            'password1': self._validated_data.get('password1', ''),
            'email': self._validated_data.get('email', ''),
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class DishTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishType
        fields = '__all__'

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'

class DishSerializer(serializers.ModelSerializer):
    host = UserSerializer(read_only=True)
    dish_type = DishTypeSerializer(many=True)
    recipes = RecipeSerializer(many=True)
    ingredients = IngredientsSerializer(many=True)
    class Meta: 
        model = Dish
        fields = '__all__'
        depth = 1
    
    def create(self, validated_data):
        # Extract data for related models
        dish_type_data = validated_data.pop('dish_type')
        recipes_data = validated_data.pop('recipes')
        ingredients_data = validated_data.pop('ingredients')
        print(dish_type_data)
        # Create the Dish instance without related objects
        dish = Dish.objects.create(**validated_data)

        # Create and associate related DishType objects
        for dish_type_item in dish_type_data:
            dish_type, created = DishType.objects.get_or_create(dish=dish ,**dish_type_item)
            dish.dish_type.add(dish_type)

        # Create and associate related Recipe objects
        for recipe_item in recipes_data:
            recipe = Recipe.objects.create(dish=dish,**recipe_item)
            dish.recipes.add(recipe)

        # Create and associate related Ingredients objects
        for ingredients_item in ingredients_data:
            ingredient, created = Ingredients.objects.get_or_create(dish=dish,**ingredients_item)
            dish.ingredients.add(ingredient)
        dish.save()
        return dish

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'