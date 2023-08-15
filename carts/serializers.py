from django.db import transaction
from rest_framework import serializers

from carts.models import Cart, CartItem




class CartItemSerializer(serializers.ModelSerializer):


    class Meta:
        model = CartItem
        fields = ('id', 'product', 'quantity', 'price', 'cart', 'created_at', 'updated_at', 'TAX_AMOUNT',)
        read_only_fields = ('id', 'cart', 'TAX_AMOUNT',)

    def create(self, validated_data):
        print(validated_data)
        if CartItem.objects.filter(cart=validated_data['cart'],product=validated_data['product']).exists():
            objj = CartItem.objects.get(cart=validated_data['cart'],product=validated_data['product'])
            objj.quantity+=validated_data['quantity']
            objj.save()
            return objj
        else:
            obj = CartItem.objects.create(**validated_data)
            obj.save()
            return obj
        

class CartSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ('id', 'user', 'total','items')
        read_only_fields = ('id', 'user',)
    
    def get_items(self,instance):
        cart = CartItem.objects.filter(cart=instance)
        cart_ser = CartItemSerializer(cart,many=True)
        return cart_ser.data


