from django.db.models import Q
from rest_framework import permissions

from shop.models import Store, StoreManager


class IsStoreOwner(permissions.BasePermission):
    """
    Custom permission to only allow seller or both user type of an object to edit it.
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Owner").exists():
            return True
        return False

    # def has_object_permission(self, request, view, obj):
    #     # Read permissions are allowed to any request,
    #     # so we'll always allow GET, HEAD or OPTIONS requests.
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #
    #     # Write permissions are only allowed to the owner of the suggestedcategory.
    #     return obj.created_by_id == request.user.id


class IsBuyerInTheOrder(permissions.BasePermission):
    """
    Custom permission to only allow seller or both user type of an object to edit it.
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(name="buyer").exists():
            return True
        return False

    def has_object_permission(self, request, view, obj):

        # Write permissions are only allowed to the owner of the suggestedcategory.
        return obj.buyer_id == request.user.id


class IsStoreAdmin(permissions.BasePermission):
    """
    Custom permission to only allow seller or both user type of an object to edit it.
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Admin").exists():
            return True
        return False

    # def has_object_permission(self, request, view, obj):
    #     # Read permissions are allowed to any request,
    #     # so we'll always allow GET, HEAD or OPTIONS requests.
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #
    #     # Write permissions are only allowed to the owner of the suggestedcategory.
    #     return obj.created_by_id == request.user.id


class IsStoreAdminOrManager(permissions.BasePermission):
    """
    Custom permission to only allow seller or both user type of an object to edit it.
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(Q(name__in="Admin") | Q(name="manage store")).exists():
            return True
        return False

    # def has_object_permission(self, request, view, obj):
    #     # Read permissions are allowed to any request,
    #     # so we'll always allow GET, HEAD or OPTIONS requests.
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #
    #     # Write permissions are only allowed to the owner of the suggestedcategory.
    #     return obj.created_by_id == request.user.id