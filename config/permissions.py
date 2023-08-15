from django.db.models import Q
from rest_framework import permissions


class IsBuyerOrBoth(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(name="buyer").exists():
            return True
        return False


class IsSellerOrBoth(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(name="seller").exists():
            return True
        return False
