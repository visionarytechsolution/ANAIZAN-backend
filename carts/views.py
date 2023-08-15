from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from carts.models import Cart, CartItem
from carts.permissions import IsBuyerAndOwnerOfCart, IsBuyerAndOwnerOfCartItem
from carts.serializers import CartItemSerializer, CartSerializer

# Create your views here.

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = []
    # authentication_classes = []
    permission_classes = [permissions.IsAuthenticated, IsBuyerAndOwnerOfCart | permissions.IsAdminUser]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.groups.filter(name="Order Manager").exists():
                return queryset.all()
            else:
                return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        print("Hello world")
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        pass


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['product', 'quantity',]
    # authentication_classes = []
    permission_classes = [permissions.IsAuthenticated, IsBuyerAndOwnerOfCartItem | permissions.IsAdminUser]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.groups.filter(name="Order Manager").exists():
                return queryset.all()
            else:
                return queryset.filter(cart__user=self.request.user)

    def perform_create(self, serializer):
        cart = Cart.objects.get(user=self.request.user)
        serializer.save(cart=cart)
