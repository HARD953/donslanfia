from rest_framework import permissions
from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
 
class IsSuperAdminAuthenticated(BasePermission):
    def has_permission(self, request, view):
    # Ne donnons l’accès qu’aux utilisateurs  Superadministrateurs authentifiés
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser and request.user.is_active and request.user.is_staff)

class IsAdminAuthenticated(BasePermission):
    def has_permission(self, request, view):
    # Ne donnons l’accès qu’aux utilisateurs administrateurs authentifiés
        return bool(request.user and request.user.is_authenticated and request.user.is_user  and request.user.is_active and request.user.is_staff)

class IsAgentAuthenticated(BasePermission):
    def has_permission(self, request, view):
    # Ne donnons l’accès qu’aux utilisateurs administrateurs authentifiés
        return bool(request.user and request.user.is_authenticated and request.user.is_agent or request.user.is_superuser and request.user.is_active and request.user.is_staff)