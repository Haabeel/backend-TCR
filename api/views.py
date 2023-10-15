import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import isHostOrReadOnly, isAdminOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser
# User views
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
    
        if request.data.get('username') != instance.username:
            return super().update(request, *args, **kwargs)
        else:
            request.data.pop('username', None)
    
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        print(request.data)
        if request.data.get('username') == instance.username:
            request.data.pop('username', None)
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
# Dish views
class DishListCreateView(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)

class DishRetrieveView(generics.RetrieveAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    lookup_field = 'pk'
    permission_classes = [isHostOrReadOnly]
class DishUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

class DishRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, isHostOrReadOnly]

    def get(self, request,*args, **kwargs):
        return super().get(request, *args, **kwargs)

# DishType views
class DishTypeCreateView(generics.ListCreateAPIView):
    queryset = DishType.objects.all()
    serializer_class = DishTypeSerializer

    def perform_create(self, serializer):
        serializer.save()

class DishTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DishType.objects.all()
    serializer_class = DishTypeSerializer
    permission_classes = [IsAuthenticated, isHostOrReadOnly]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

# Recipe views
class RecipeCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def perform_create(self, serializer):
        serializer.save()

class RecipeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated, isHostOrReadOnly]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

# Ingredient views
class IngredientCreateView(generics.ListCreateAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer

    def perform_create(self, serializer):
        serializer.save()

class IngredientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = [isHostOrReadOnly]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ImageListCreateView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser,)

class ImageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser,)

    def get(self,request,*args,**kwargs):
        return super().get(request, *args, **kwargs)