from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from orders.models import Order
from orders.permissions import IsBuyerInTheOrder, IsStoreAdminOrManager, IsStoreOwner
from orders.serializers import OrderSerializer

# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['product', 'quantity', 'order_status', 'order_status', 'order_paid_status',]
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
                return queryset.filter(product__store__owner_id=self.request.user)
            elif self.request.user.groups.filter(name__in=['Store owner', 'Admin', 'manage store']).exists():
                return queryset.filter(product__store__storemanager__user_id=self.request.user.id)
            elif self.request.user.groups.filter(name__in=['Administrator', 'Order Manager']).exists():
                return queryset.all()
            else:
                return queryset.filter(created_by=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        order = self.get_object()
        order.delete = True
        order.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
