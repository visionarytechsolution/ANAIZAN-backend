from rest_framework import serializers

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'address', 'product', 'quantity', 'price', 'order_status', 'created_at', 'created_by', 'updated_at',
                  'updated_by', 'TAX_AMOUNT', 'delivered_at', 'payment_method', 'order_paid_status', 'transaction_id',)
        read_only_fields = ('id', 'order_paid_status', 'created_at', 'created_by', 'updated_at', 'updated_by',)
