from django.http import Http404
from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import pagination, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from config.models import Authorization, AuthorizationType, AzCity, AzCountry, AzPackage, AzState, MeasureUnit, TimeUnit
from config.permissions import IsSellerOrBoth
from config.serializers import (
    AdminAuthorizationSerializer,
    AdminAuthorizationTypeSerializer,
    AdminAzCitySerializer,
    AdminAzCountrySerializer,
    AdminAzPackageSerializer,
    AdminAzStateSerializer,
    AdminMeasureUnitSerializer,
    AdminTimeUnitSerializer,
    BuyerAzCitySerializer,
    BuyerAzCountrySerializer,
    BuyerAzPackageSerializer,
    BuyerAzStateSerializer,
    BuyerMeasureUnitSerializer,
    BuyerTimeUnitSerializer,
    SellerAzCitySerializer,
    SellerAzCountrySerializer,
    SellerAzPackageSerializer,
    SellerAzStateSerializer,
    SellerMeasureUnitSerializer,
    SellerTimeUnitSerializer,
)

# Create your views here.


""" ########################################### ADMIN PART ################################################ """


""" *************************** AzPackage instance ************************** """


class AdminAzPackageListView(ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = AzPackage.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = AdminAzPackageSerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_fields = ('package_name', 'package_code', 'description', 'is_active', 'created_by', 'updated_by')


class AdminAzPackageCreateView(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminAzPackageSerializer


class AdminAzPackageDetailView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            return AzPackage.objects.get(pk=pk)
        except AzPackage.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        package = self.get_object(pk)
        serializer = AdminAzPackageSerializer(package)
        return Response(serializer.data)

    def put(self, request, pk):
        package = self.get_object(pk)
        serializer = AdminAzPackageSerializer(package, data=request.data)
        if serializer.is_valid():
            serializer.save(updated_by=request.user.id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        package = self.get_object(pk)
        package.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" *************************** AzCountry instance ************************** """


class AdminAzCountryListView(ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = AzCountry.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = AdminAzCountrySerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_fields = ('country_name', 'country_code', 'is_active', 'currency', 'created_by', 'updated_by',)


class AdminAzCountryCreateView(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminAzCountrySerializer


class AdminAzCountryDetailView(APIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminAzCountrySerializer

    def get_object(self, pk):
        try:
            return AzCountry.objects.get(pk=pk)
        except AzCountry.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        country = self.get_object(pk)
        serializer = AdminAzCountrySerializer(country)
        return Response(serializer.data)

    def put(self, request, pk):
        country = self.get_object(pk)
        serializer = self.serializer_class(country, data=request.data)
        if serializer.is_valid():
            serializer.save(updated_by=request.user.id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        country = self.get_object(pk)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" ******************************************* AzState instance **************************************** """


class AdminAzStateListView(ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = AzState.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = AdminAzStateSerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_fields = ('state_name', 'state_code', 'country', 'is_active', 'created_by', 'updated_by',)


class AdminAzStateCreateView(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminAzStateSerializer


class AdminAzStateDetailView(APIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminAzStateSerializer

    def get_object(self, pk):
        try:
            return AzState.objects.get(pk=pk)
        except AzState.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        state = self.get_object(pk)
        serializer = self.serializer_class(state)
        return Response(serializer.data)

    def put(self, request, pk):
        state = self.get_object(pk)
        serializer = self.serializer_class(state, data=request.data)
        if serializer.is_valid():
            serializer.save(updated_by=request.user.id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        state = self.get_object(pk)
        state.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" ******************************************* AzCity instance **************************************** """


class AdminAzCityListView(ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = AzCity.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = AdminAzCitySerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_fields = ('city_name', 'city_code', 'state', 'is_active', 'created_by', 'updated_by',)


class AdminAzCityCreateView(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminAzCitySerializer


class AdminAzCityDetailView(APIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminAzCitySerializer

    def get_object(self, pk):
        try:
            return AzCity.objects.get(pk=pk)
        except AzCity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        city = self.get_object(pk)
        serializer = self.serializer_class(city)
        return Response(serializer.data)

    def put(self, request, pk):
        city = self.get_object(pk)
        serializer = self.serializer_class(city, data=request.data)
        if serializer.is_valid():
            serializer.save(updated_by=request.user.id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        city = self.get_object(pk)
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" ******************************************* MeasureUnit instance **************************************** """


class AdminMeasureUnitListView(ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = MeasureUnit.objects.all()
    serializer_class = AdminMeasureUnitSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('unit', 'code', 'is_active', 'created_by', 'updated_by',)


class AdminMeasureUnitCreateView(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminMeasureUnitSerializer


class AdminMeasureUnitDetailView(APIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminMeasureUnitSerializer

    def get_object(self, pk):
        try:
            return MeasureUnit.objects.get(pk=pk)
        except MeasureUnit.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        measure_unit = self.get_object(pk)
        serializer = self.serializer_class(measure_unit)
        return Response(serializer.data)

    def put(self, request, pk):
        measure_unit = self.get_object(pk)
        serializer = self.serializer_class(measure_unit, data=request.data)
        if serializer.is_valid():
            serializer.save(updated_by=request.user.id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        measure_unit = self.get_object(pk)
        measure_unit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" ******************************************* TimeUnit instance **************************************** """


class AdminTimeUnitListView(ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = TimeUnit.objects.all()
    serializer_class = AdminTimeUnitSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('unit', 'code', 'is_active', 'created_by', 'updated_by',)


class AdminTimeUnitCreateView(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminTimeUnitSerializer


class AdminTimeUnitDetailView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            return TimeUnit.objects.get(pk=pk)
        except TimeUnit.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        time_unit = self.get_object(pk)
        serializer = AdminTimeUnitSerializer(time_unit)
        return Response(serializer.data)

    def put(self, request, pk):
        time_unit = self.get_object(pk)
        serializer = AdminTimeUnitSerializer(time_unit, data=request.data)
        if serializer.is_valid():
            serializer.save(updated_by=request.user.id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        time_unit = self.get_object(pk)
        time_unit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" ******************************************* AuthorizationType instance **************************************** """


class AdminAuthorizationTypeListView(ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = AuthorizationType.objects.all()
    serializer_class = AdminAuthorizationTypeSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name', 'code', 'created_by', 'updated_by',)


class AdminAuthorizationTypeDetailView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            return AuthorizationType.objects.get(pk=pk)
        except AuthorizationType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        authorization_type = self.get_object(pk)
        serializer = AdminTimeUnitSerializer(authorization_type)
        return Response(serializer.data)


""" ******************************************* Authorization instance **************************************** """


class AdminAuthorizationListView(ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Authorization.objects.all()
    serializer_class = AdminAuthorizationSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('type', 'is_active', 'created_by', 'updated_by',)


class AdminAuthorizationCreateView(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminAuthorizationSerializer


class AdminAuthorizationDetailView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            return Authorization.objects.get(pk=pk)
        except Authorization.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        authorization = self.get_object(pk)
        serializer = AdminAuthorizationSerializer(authorization)
        return Response(serializer.data)

    def put(self, request, pk):
        authorization = self.get_object(pk)
        serializer = AdminAuthorizationSerializer(authorization, data=request.data)
        if serializer.is_valid():
            serializer.save(updated_by=request.user.id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        authorization = self.get_object(pk)
        authorization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" ########################################### SELLER PART ################################################ """


""" *************************** AzPackage instance ************************** """


class SellerAzPackageListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsSellerOrBoth]
    filter_backends = (filters.DjangoFilterBackend,)
    queryset = AzPackage.seller_objects.all()
    serializer_class = SellerAzPackageSerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_fields = ('package_name', 'description',)


class SellerAzPackageDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsSellerOrBoth]
    serializer_class = SellerAzPackageSerializer

    def get_object(self, pk):
        try:
            return AzPackage.seller_objects.get(pk=pk)
        except AzPackage.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        package = self.get_object(pk)
        serializer = self.serializer_class(package)
        return Response(serializer.data)


""" *************************** AzCountry instance ************************** """


class SellerAzCountryListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsSellerOrBoth]
    filter_backends = (filters.DjangoFilterBackend,)
    queryset = AzCountry.seller_objects.all()
    serializer_class = SellerAzCountrySerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_fields = ('country_name', 'currency',)


class SellerAzCountryDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsSellerOrBoth]
    serializer_class = SellerAzCountrySerializer

    def get_object(self, pk):
        try:
            return AzCountry.seller_objects.get(pk=pk)
        except AzCountry.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        country = self.get_object(pk)
        serializer = self.serializer_class(country)
        return Response(serializer.data)


""" ******************************************* AzState instance **************************************** """


class SellerAzStateListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsSellerOrBoth]
    queryset = AzState.seller_objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = SellerAzStateSerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_fields = ('state_name', 'country',)


class SellerAzStateDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsSellerOrBoth]
    serializer_class = SellerAzStateSerializer

    def get_object(self, pk):
        try:
            return AzState.seller_objects.get(pk=pk)
        except AzState.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        state = self.get_object(pk)
        serializer = self.serializer_class(state)
        return Response(serializer.data)


""" ******************************************* AzCity instance **************************************** """


class SellerAzCityListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsSellerOrBoth]
    queryset = AzCity.seller_objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = SellerAzCitySerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_fields = ('city_name', 'state',)


class SellerAzCityDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsSellerOrBoth]
    serializer_class = SellerAzCitySerializer

    def get_object(self, pk):
        try:
            return AzCity.seller_objects.get(pk=pk)
        except AzCity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        city = self.get_object(pk)
        serializer = self.serializer_class(city)
        return Response(serializer.data)


""" ******************************************* MeasureUnit instance **************************************** """


class SellerMeasureUnitListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsSellerOrBoth]
    queryset = MeasureUnit.seller_objects.all()
    serializer_class = SellerMeasureUnitSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('unit',)


class SellerMeasureUnitDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsSellerOrBoth]
    serializer_class = SellerMeasureUnitSerializer

    def get_object(self, pk):
        try:
            return MeasureUnit.seller_objects.get(pk=pk)
        except MeasureUnit.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        measure_unit = self.get_object(pk)
        serializer = self.serializer_class(measure_unit)
        return Response(serializer.data)


""" ******************************************* TimeUnit instance **************************************** """


class SellerTimeUnitListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsSellerOrBoth]
    queryset = TimeUnit.seller_objects.all()
    serializer_class = SellerTimeUnitSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('unit',)


class SellerTimeUnitDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsSellerOrBoth]

    def get_object(self, pk):
        try:
            return TimeUnit.seller_objects.get(pk=pk)
        except TimeUnit.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        time_unit = self.get_object(pk)
        serializer = SellerTimeUnitSerializer(time_unit)
        return Response(serializer.data)


""" ########################################### SIMPLE USER OR BUYER PART ################################################ """


""" *************************** AzPackage instance ************************** """


class BuyerAzPackageListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    queryset = AzPackage.buyer_objects.all()
    serializer_class = BuyerAzPackageSerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_fields = ('package_name', 'description',)


class BuyerAzPackageDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BuyerAzPackageSerializer

    def get_object(self, pk):
        try:
            return AzPackage.buyer_objects.get(pk=pk)
        except AzPackage.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        package = self.get_object(pk)
        serializer = self.serializer_class(package)
        return Response(serializer.data)


""" *************************** AzCountry instance ************************** """


class BuyerAzCountryListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = AzCountry.buyer_objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = BuyerAzCountrySerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_fields = ('country_name', 'currency',)


class BuyerAzCountryDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BuyerAzCountrySerializer

    def get_object(self, pk):
        try:
            return AzCountry.buyer_objects.get(pk=pk)
        except AzCountry.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        country = self.get_object(pk)
        serializer = self.serializer_class(country)
        return Response(serializer.data)


""" ******************************************* AzState instance **************************************** """


class BuyerAzStateListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = AzState.buyer_objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = BuyerAzStateSerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_fields = ('state_name', 'country',)


class BuyerAzStateDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BuyerAzStateSerializer

    def get_object(self, pk):
        try:
            return AzState.buyer_objects.get(pk=pk)
        except AzState.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        state = self.get_object(pk)
        serializer = self.serializer_class(state)
        return Response(serializer.data)


""" ******************************************* AzCity instance **************************************** """


class BuyerAzCityListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = AzCity.buyer_objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = BuyerAzCitySerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_fields = ('city_name', 'state',)


class BuyerAzCityDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BuyerAzCitySerializer

    def get_object(self, pk):
        try:
            return AzCity.buyer_objects.get(pk=pk)
        except AzCity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        city = self.get_object(pk)
        serializer = self.serializer_class(city)
        return Response(serializer.data)


""" ******************************************* MeasureUnit instance **************************************** """


class BuyerMeasureUnitListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = MeasureUnit.buyer_objects.all()
    serializer_class = BuyerMeasureUnitSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('unit',)


class BuyerMeasureUnitDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BuyerMeasureUnitSerializer

    def get_object(self, pk):
        try:
            return MeasureUnit.buyer_objects.get(pk=pk)
        except MeasureUnit.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        measure_unit = self.get_object(pk)
        serializer = self.serializer_class(measure_unit)
        return Response(serializer.data)


""" ******************************************* TimeUnit instance **************************************** """


class BuyerTimeUnitListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = TimeUnit.buyer_objects.all()
    serializer_class = BuyerTimeUnitSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('unit',)


class BuyerTimeUnitDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return TimeUnit.buyer_objects.get(pk=pk)
        except TimeUnit.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        time_unit = self.get_object(pk)
        serializer = BuyerTimeUnitSerializer(time_unit)
        return Response(serializer.data)




