from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from shipping.models import Address, Shipping
from shipping.permissions import IsBuyerInTheOrder, IsStoreAdminOrManager, IsStoreOwner
from shipping.serializers import AddressSerializer, ShippingSerializer

# Create your views here.

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['country', 'state', 'city', 'address_line_1', 'address_line_2', 'zip_code',]
    # authentication_classes = []
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class ShippingViewSet(viewsets.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['reference_number', 'amount', 'status', 'delivery_personnel',] # order
    # authentication_classes = []
    permission_classes = [permissions.IsAuthenticated, IsStoreOwner | IsStoreAdminOrManager | IsBuyerInTheOrder]

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsBuyerInTheOrder]
        else:
            permission_classes = [permissions.IsAuthenticated, IsStoreOwner | IsStoreAdminOrManager | IsBuyerInTheOrder]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.groups.filter(name__in=['Store owner']).exists():
                return queryset.filter(order__product__store__owner_id=self.request.user)
            elif self.request.user.groups.filter(name__in=['Store owner', 'Admin', 'manage store']).exists():
                return queryset.filter(order__product__store__storemanager__user_id=self.request.user.id)
            elif self.request.user.groups.filter(name__in=['Administrator', 'Order Manager']).exists():
                return queryset.all()
            else:
                return queryset.filter(order__created_by_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        pass
