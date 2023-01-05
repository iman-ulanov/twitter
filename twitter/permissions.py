from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'GET':
            return True
        if request.user.is_authenticated:
            return True





class IsTweetOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return obj == request.user
