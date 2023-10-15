from rest_framework import permissions
from .models import Dish
class isHostOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if isinstance(obj, Dish):
            return obj.host == request.user
        if not isinstance(obj, Dish):
            return obj.dish_set.filter(host = request.user).exists()
        return obj.host == request.user
class isAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_staff:
            return True
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj == request.user
        return False