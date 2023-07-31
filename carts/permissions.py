from rest_framework import permissions


class IsBuyerAndOwnerOfCart(permissions.BasePermission):
    """
    Custom permission to only allow seller or both user type of an object to edit it.
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(name="buyer").exists():
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.

        # Write permissions are only allowed to the owner of the suggestedcategory.
        return obj.user == request.user


class IsBuyerAndOwnerOfCartItem(permissions.BasePermission):
    """
    Custom permission to only allow seller or both user type of an object to edit it.
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(name="buyer").exists():
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.

        # Write permissions are only allowed to the owner of the suggestedcategory.
        return obj.cart.user == request.user
