from rest_framework import serializers

from shipping.models import Address, Shipping


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('id', 'country', 'state', 'city', 'address_line_1', 'address_line_2', 'zip_code',
                  'created_at', 'created_by', 'updated_at', 'updated_by',)
        read_only_fields = ('id', 'created_at', 'created_by', 'updated_at', 'updated_by',)


class ShippingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipping
        fields = ('id', 'order', 'reference_number', 'amount', 'status', 'delivery_personnel',
                  'created_by', 'created_at', 'updated_at', 'updated_by',)
        read_only_fields = ('id', 'order', 'created_at', 'created_by', 'updated_at', 'updated_by',)
