from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from accounts.models import CustomUser
from products.models import Product, ProductMedia, ProductPrice,ProductSlider
from products.permissions import IsProductManager, IsStoreAdmin, IsStoreManager, IsStoreOwner
from products.serializers import ProductMediaSerializer, ProductPriceSerializer, ProductSerializer,ProductSliderSerializer

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['store', 'category', 'name', 'description', 'is_active', ]
    # authentication_classes = []
    permission_classes = []

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]

        else:
            permission_classes = [IsStoreOwner | IsStoreAdmin | IsProductManager | IsStoreManager | permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.groups.filter(name__in=["Administrator", "Shop Manager", "Vendor Manager", "Custom Manager",
                                                         "Sale manager", "Content Manager", "Blog Manager", "Order Manager",
                                                         "Develivery Manager", "Support Manager", "Ads Manager",
                                                         "SEO Manager"]).exists():
                return queryset.all()
            elif self.request.user.groups.filter(
                    name__in=["Admin", "manage store", "manage products", "Editor", "Custom"]).exists():
                return queryset.filter(store__storemanager__user_id=self.request.user.id)
        return queryset.filter(is_active=True)

    def perform_create(self, serializer):
        print("hello world")
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        product.delete = True
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductPriceViewSet(viewsets.ModelViewSet):
    queryset = ProductPrice.objects.all()
    serializer_class = ProductPriceSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['product', 'quantity_min', 'quantity_max', 'price', 'delivery_time', 'time_unit', 'is_active', ]
    # authentication_classes = []
    permission_classes = []

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsStoreOwner | IsStoreAdmin | IsProductManager | IsStoreManager | permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.groups.filter(name="Owner").exists():
                return queryset.filter(product__store__owner_id=self.request.user.id)
            elif self.request.user.groups.filter(name__in=["Administrator", "Shop Manager", "Vendor Manager", "Custom Manager",
                                                           "Sale manager", "Content Manager", "Blog Manager", "Order Manager",
                                                           "Develivery Manager", "Support Manager", "Ads Manager",
                                                           "SEO Manager"]).exists():
                return queryset.all()
            elif self.request.user.groups.filter(
                    name__in=["Admin", "manage store", "manage products", "Editor", "Custom"]).exists():
                return queryset.filter(product__store__storemanager__user_id=self.request.user.id)
        return queryset.filter(is_active=True)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        product.delete = True
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductMediaViewSet(viewsets.ModelViewSet):
    queryset = ProductMedia.objects.all()
    serializer_class = ProductMediaSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['product', 'is_active', ]
    # authentication_classes = []
    permission_classes = []

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsStoreOwner | IsStoreAdmin | IsProductManager | IsStoreManager | permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.groups.filter(name="Owner").exists():
                return queryset.filter(product__store__owner_id=self.request.user.id)
            elif self.request.user.groups.filter(name__in=["Administrator", "Shop Manager", "Vendor Manager", "Custom Manager",
                                                           "Sale manager", "Content Manager", "Blog Manager", "Order Manager",
                                                           "Develivery Manager", "Support Manager", "Ads Manager",
                                                           "SEO Manager"]).exists():
                return queryset.all()
            elif self.request.user.groups.filter(
                    name__in=["Admin", "manage store", "manage products", "Editor", "Custom"]).exists():
                return queryset.filter(product__store__storemanager__user_id=self.request.user.id)
        return queryset.filter(is_active=True)

    def perform_create(self, serializer):
        print("Hello world")
        print(self.request.user)
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        product.delete = True
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)





class ProductSliderViewSet(viewsets.ModelViewSet):
    queryset = ProductSlider.objects.all()
    serializer_class = ProductSliderSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['product', 'is_active', ]
    # authentication_classes = []
    permission_classes = []

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsStoreOwner | IsStoreAdmin | IsProductManager | IsStoreManager | permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.groups.filter(name="Owner").exists():
                return queryset.filter(product__store__owner_id=self.request.user.id)
            elif self.request.user.groups.filter(name__in=["Administrator", "Shop Manager", "Vendor Manager", "Custom Manager",
                                                           "Sale manager", "Content Manager", "Blog Manager", "Order Manager",
                                                           "Develivery Manager", "Support Manager", "Ads Manager",
                                                           "SEO Manager"]).exists():
                return queryset.all()
            elif self.request.user.groups.filter(
                    name__in=["Admin", "manage store", "manage products", "Editor", "Custom"]).exists():
                return queryset.filter(product__store__storemanager__user_id=self.request.user.id)
        return queryset.filter(is_active=True)
