from django.db import transaction
from rest_framework import serializers

from config.models import Authorization, AuthorizationType, AzCity, AzCountry, AzPackage, AzState, MeasureUnit, TimeUnit

""" ########################################### ADMIN PART ############################################### """


""" *********************** AzPackage instance ********************** """


class AdminAzPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AzPackage
        fields = '__all__'
        read_only_fields = ('id', 'created_by', 'updated_by',)

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user.id
            return AzPackage.objects.create(**validated_data, created_by=user)
        else:
            pass


""" *************************** AzCountry instance ************************** """


class AdminAzCountrySerializer(serializers.ModelSerializer):
        class Meta:
            model = AzCountry
            fields = '__all__'
            read_only_fields = ('country_id', 'created_by', 'updated_by',)

        def create(self, validated_data):
            user = None
            request = self.context.get("request")
            if request and hasattr(request, "user"):
                user = request.user.id
                return AzCountry.objects.create(**validated_data, created_by=user)
            else:
                pass


""" *************************** AzState instance ************************** """


class AdminAzStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AzState
        fields = ['state_id', 'state_id', 'state_name', 'state_code', 'country', 'is_active', 'created_at', 'created_by',
                  'updated_at', 'updated_by']
        read_only_fields = ('state_id', 'created_by', 'updated_by',)

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user.id
            return AzState.objects.create(**validated_data, created_by=user)
        else:
            pass


""" *************************** AzCity instance ************************** """


class AdminAzCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AzCity
        fields = ['city_id', 'city_name', 'city_code', 'state', 'is_active', 'created_at', 'created_by',
                  'updated_at', 'updated_by']
        read_only_fields = ('city_id', 'created_by', 'updated_by',)

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user.id
            return AzCity.objects.create(**validated_data, created_by=user)
        else:
            pass


""" *************************** MeasureUnit instance ************************** """


class AdminMeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        fields = ['id', 'unit', 'code', 'created_at', 'is_active', 'created_by', 'updated_at', 'updated_by']
        read_only_fields = ('id', 'created_by', 'updated_by')

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user.id
            return MeasureUnit.objects.create(**validated_data, created_by=user)
        else:
            pass


""" *************************** TimeUnit instance ************************** """


class AdminTimeUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeUnit
        fields = '__all__'
        read_only_fields = ('id', 'created_by', 'updated_by')

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user.id
            return TimeUnit.objects.create(**validated_data, created_by=user)
        else:
            pass


""" *************************** AuthorizationType instance ************************** """


class AdminAuthorizationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorizationType
        fields = '__all__'
        read_only_fields = ('id', 'created_by', 'updated_by')

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user.id
            return Authorization.objects.create(**validated_data, created_by=user)
        else:
            pass


""" *************************** Authorization instance ************************** """


class AdminAuthorizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authorization
        fields = '__all__'
        read_only_fields = ('id', 'created_by', 'updated_by')

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user.id
            return Authorization.objects.create(**validated_data, created_by=user)
        else:
            pass


""" ########################################### SELLER PART ############################################### """


""" *********************** AzPackage instance ********************** """


class SellerAzPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AzPackage
        fields = '__all__'
        read_only_fields = ('id', 'created_by', 'is_active', 'user_type', 'updated_by',)


""" *************************** AzCountry instance ************************** """


class SellerAzCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AzCountry
        fields = ['country_id', 'country_name', 'country_code', 'is_active', 'currency',
                  'created_at', 'created_by', 'updated_at', 'updated_by']
        read_only_fields = ('country_id', 'is_active', 'created_by', 'updated_by',)


""" *************************** AzState instance ************************** """


class SellerAzStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AzState
        fields = ['state_id', 'state_id', 'state_name', 'state_code', 'country', 'is_active', 'created_at', 'created_by',
                  'updated_at', 'updated_by']
        read_only_fields = ('state_id', 'is_active', 'created_by', 'updated_by',)


""" *************************** AzCity instance ************************** """


class SellerAzCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AzCity
        fields = ['city_id', 'city_name', 'city_code', 'state', 'is_active', 'created_at', 'created_by',
                  'updated_at', 'updated_by']
        read_only_fields = ('city_id', 'is_active', 'created_by', 'updated_by',)


""" *************************** MeasureUnit instance ************************** """


class SellerMeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        fields = ['id', 'unit', 'code', 'created_at', 'is_active', 'created_by', 'updated_at', 'updated_by']
        read_only_fields = ('id', 'is_active', 'created_by', 'updated_by')


""" *************************** TimeUnit instance ************************** """


class SellerTimeUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeUnit
        fields = '__all__'
        read_only_fields = ('id', 'is_active', 'created_by', 'updated_by')


""" ########################################### BUYER PART ############################################### """


""" *********************** AzPackage instance ********************** """


class BuyerAzPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AzPackage
        fields = '__all__'
        read_only_fields = ('id', 'created_by', 'is_active', 'user_type', 'updated_by',)


""" *************************** AzCountry instance ************************** """


class BuyerAzCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AzCountry
        fields = ['country_id', 'country_name', 'country_code', 'is_active', 'currency',
                  'created_at', 'created_by', 'updated_at', 'updated_by']
        read_only_fields = ('country_id', 'is_active', 'created_by', 'updated_by',)


""" *************************** AzState instance ************************** """


class BuyerAzStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AzState
        fields = ['state_id', 'state_id', 'state_name', 'state_code', 'country', 'is_active', 'created_at',
                  'created_by',
                  'updated_at', 'updated_by']
        read_only_fields = ('state_id', 'is_active', 'created_by', 'updated_by',)


""" *************************** AzCity instance ************************** """


class BuyerAzCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AzCity
        fields = ['city_id', 'city_name', 'city_code', 'state', 'is_active', 'created_at', 'created_by',
                  'updated_at', 'updated_by']
        read_only_fields = ('city_id', 'is_active', 'created_by', 'updated_by',)


""" *************************** MeasureUnit instance ************************** """


class BuyerMeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        fields = ['id', 'unit', 'code', 'created_at', 'is_active', 'created_by', 'updated_at', 'updated_by']
        read_only_fields = ('id', 'is_active', 'created_by', 'updated_by')


""" *************************** TimeUnit instance ************************** """


class BuyerTimeUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeUnit
        fields = '__all__'
        read_only_fields = ('id', 'is_active', 'created_by', 'updated_by')