from django.contrib.auth.models import Group
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import CustomUser
from shop.models import Domain, Store, StoreManager
from shop.permissions import IsStoreAdmin, IsStoreAdminOrManager, IsStoreOwner
from shop.serializers import DomainSerializer, StoreManagerSerializer, StoreSerializer

# Create your views here.


class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsStoreOwner | IsStoreAdminOrManager | permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        domain = self.get_object()
        domain.delete = True
        domain.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['name', 'domains', 'owner', 'is_active', ]
    # authentication_classes = []
    permission_classes = []

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsStoreOwner | IsStoreAdminOrManager | permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.groups.filter(name="Owner").exists():
                return queryset.filter(owner_id=self.request.user.id)
            elif self.request.user.groups.filter(name__in=["Admin", "manage store", "manage products", "Editor", "Custom"]).exists():
                return queryset.filter(storemanager__user_id=self.request.user)
            elif self.request.user.groups.filter(name__in=["Administrator", "Shop Manager", ]).exists():
                return queryset.all()
            else:
                return queryset.filter(is_active=True)
        return queryset.filter(is_active=True)

    def destroy(self, request, *args, **kwargs):
        store = self.get_object()
        store.delete = True
        store.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StoreManagerViewSet(viewsets.ModelViewSet):
    serializer_class = StoreManagerSerializer
    queryset = StoreManager.objects.all()
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['user', 'domains', 'role', 'store', ]
    # authentication_classes = []
    permission_classes = []

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsStoreOwner | IsStoreAdmin | permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            
            queryset = super().get_queryset()
            if self.request.user.groups.filter(name="Owner").exists():
                return queryset.filter(store__owner_id=self.request.user.id)
            elif self.request.user.groups.filter(name__in=["Admin", "manage store", "manage products", "Editor", "Custom"]).exists():
                return queryset.filter(user_id=self.request.user)
            elif self.request.user.groups.filter(name__in=["Administrator", "Shop Manager", ]).exists():
                return queryset.all()

        else:
            return None

    def destroy(self, request, *args, **kwargs):
        store_manager = self.get_object()
        store_manager.delete = True
        store_manager.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
