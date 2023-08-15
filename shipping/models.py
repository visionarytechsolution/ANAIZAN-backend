import uuid

from django.db import models

from accounts.models import CustomUser

# Create your models here.


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(CustomUser, related_name="address_created_by", on_delete=models.PROTECT, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    updated_by = models.ForeignKey(CustomUser, related_name="address_updated_by", blank=True, null=True, on_delete=models.PROTECT, editable=False)

    def __str__(self):
        return "Address (" + str(self.id) + ")"


# from orders.models import Order
class Shipping(models.Model):
    class ShippingStatus(models.IntegerChoices):
        DEFAULT = 1, 'Default'
        CANCEL = 2, 'Cancel'
        REFUND = 3, 'Refund'
        SUCCESS = 4, 'Success'
        PROCESSING = 5, 'Processing'
        SHIPPED = 6, 'Shipped'
        DONE = 7, 'Done'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.OneToOneField("orders.Order", on_delete=models.CASCADE)
    reference_number = models.CharField(max_length=100)
    amount = models.FloatField()
    status = models.SmallIntegerField(choices=ShippingStatus.choices, default=ShippingStatus.DEFAULT)
    delivery_personnel = models.CharField(max_length=250)
    created_by = models.ForeignKey(CustomUser, related_name="shipping_created_by", on_delete=models.PROTECT, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    updated_by = models.ForeignKey(CustomUser, related_name="shipping_updated_by", blank=True, null=True, on_delete=models.PROTECT, editable=False)

    def __str__(self):
        return "Shipping (" + str(self.id) + ")"

