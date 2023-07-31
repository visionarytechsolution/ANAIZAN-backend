from rest_framework import serializers

from shop.models import Domain, Store, StoreManager


class DomainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Domain
        fields = ('id', 'url',)
        read_only_fields = ('id',)


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ('id', 'name', 'slug', 'logo', 'domains', 'owner', 'is_active',)
        read_only_fields = ('id', 'slug',)


class StoreManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreManager
        fields = ('id', 'user', 'domains', 'role', 'store',)
        read_only_fields = ('id',)













