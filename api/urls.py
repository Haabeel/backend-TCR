from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('user/<int:pk>/', UserRetrieveUpdateDestroyView.as_view()),
    path('dishes/', DishListCreateView.as_view()),
    path('dishes/<int:pk>/', DishRetrieveView.as_view()),
    path('dishes/update/<int:pk>/', DishUpdateDestroyView.as_view()),
    path('dishes/dish_types/', DishTypeCreateView.as_view()),
    path('dishes/dish_types/<int:pk>/', DishTypeRetrieveUpdateDestroyView.as_view()),
    path('dishes/recipes/', RecipeCreateView.as_view()),
    path('dishes/recipes/<int:pk>/', RecipeRetrieveUpdateDestroyView.as_view()),
    path('dishes/ingredients/', IngredientCreateView.as_view()),
    path('dishes/ingredients/<int:pk>/', IngredientRetrieveUpdateDestroyView.as_view()),
    path('dishes/images/', ImageListCreateView.as_view()),
    path('dishes/images/<int:pk>/', ImageRetrieveUpdateDestroyView.as_view())
]