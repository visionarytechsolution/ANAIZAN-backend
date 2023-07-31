import uuid

from django.db import models

from accounts.models import CustomUser
from products.models import Product
from shipping.models import Address

# Create your models here.


# class PayMentMethod(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     method = models.CharField(max_length=100)
#
#     class Meta:
#         verbose_name = "Payment Method"
#         verbose_name_plural = "Payment Methods"
#
#     def __str__(self):
#         return str(self.method)


class OrderModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(delete=True)


class Order(models.Model):
    class OrderStatus(models.IntegerChoices):
        DEFAULT = 1, 'Default'
        CANCEL = 2, 'Cancel'
        REFUND = 3, 'Refund'
        SUCCESS = 4, 'Success'
        PROCESSING = 5, 'Processing'
        SHIPPED = 6, 'Shipped'
        DONE = 7, 'Done'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.ForeignKey(Address, null='', blank=True, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(blank=True, default=0)
    order_status = models.SmallIntegerField(choices=OrderStatus.choices, default=OrderStatus.DEFAULT)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(CustomUser, related_name="order_created_by", on_delete=models.PROTECT, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    updated_by = models.ForeignKey(CustomUser, related_name="order_updated_by", blank=True, null=True, on_delete=models.PROTECT, editable=False)

    TAX_AMOUNT = models.DecimalField(max_digits=10, default=0.00, decimal_places=2)

    delivered_at = models.DateTimeField(null=True, blank=True)

    payment_method = models.CharField(max_length=200,  default='')
    order_paid_status = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, default='')
    # payment_response = models.JSONField(blank=True, null=True)

    # extra = models.JSONField(blank=True, null=True)

    delete = models.BooleanField(default=False)

    objects = OrderModelManager()

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'buyer ' + str(self.created_by) + ' - shop (seller) ' + str(self.product.store)
