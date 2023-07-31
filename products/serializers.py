from django.db import transaction
from rest_framework import serializers

from products.models import Product, ProductMedia, ProductPrice


class ProductSerializer(serializers.ModelSerializer):

    """ serializer """

    class Meta:
        model = Product
        fields = ('id', 'store', 'category', 'name', 'description', 'sku', 'upc', 'discount', 'available',
                  'star_rating', 'likes', 'detail_desc', 'is_active', 'created_by', 'created_at', 'updated_by',
                  'updated_at',)
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_by', 'updated_at',)

    


class ProductPriceSerializer(serializers.ModelSerializer):

    """ serializer """

    class Meta:
        model = ProductPrice
        fields = ('id', 'product', 'quantity_min', 'quantity_max', 'price', 'delivery_time', 'time_unit', 'discount_price', 'is_active',
                  'created_by', 'created_at', 'updated_by', 'updated_at',)
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_by', 'updated_at',)


class ProductMediaSerializer(serializers.ModelSerializer):

    """ serializer """

    class Meta:
        model = ProductMedia
        fields = ('id', 'product', 'media', 'display_order', 'is_active', 'created_by', 'created_at', 'updated_by', 'updated_at',)
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_by', 'updated_at',)
