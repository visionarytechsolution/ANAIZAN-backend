from django.db.models import Q
from django.http import Http404
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import CustomUser
from category.models import Category, SuggestedCategory
from category.permissions import IsStoreAdminOrManager, IsStoreOwner
from category.serializers import CategorySerializer, SuggestedCategorySerializer

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['code', 'name', 'description', 'category', 'is_active', ]
    # authentication_classes = []
    permission_classes = []

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
            #permission_classes = []
        else:
            permission_classes = [permissions.IsAdminUser]
            #permission_classes = []
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.groups.filter(name__in=["Administrator", "Shop Manager", "Vendor Manager", "Custom Manager",
                                                         "Sale manager", "Content Manager", "Blog Manager", "Order Manager",
                                                         "Develivery Manager", "Support Manager", "Ads Manager",
                                                         "SEO Manager"]).exists():
                return queryset.all()
        return queryset.filter(is_active=True)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        category = self.get_object()
        category.delete = True
        category.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SuggestedCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = SuggestedCategorySerializer
    queryset = SuggestedCategory.objects.all()
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['name', 'category', ]
    # authentication_classes = []
    permission_classes = [IsStoreOwner | IsStoreAdminOrManager | permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        suggested_category = self.get_object()
        suggested_category.delete = True
        suggested_category.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
