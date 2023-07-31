from django.db import transaction
from rest_framework import serializers

from carts.models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ('id', 'user', 'total',)
        read_only_fields = ('id', 'user',)


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ('id', 'product', 'quantity', 'price', 'cart', 'created_at', 'updated_at', 'TAX_AMOUNT',)
        read_only_fields = ('id', 'cart', 'TAX_AMOUNT',)