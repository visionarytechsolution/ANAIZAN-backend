import uuid

from django.db import models

from accounts.models import CustomUser
from products.models import Product

# Create your models here.

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(CustomUser, on_delete=models.PROTECT, editable=False)
    total = models.FloatField(blank=True, default=0)

    def __str__(self):
        return str(self.user)


class CartItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(blank=True, default=0)
    cart = models.ForeignKey('Cart', related_name="cart_item", editable=False, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    TAX_AMOUNT = models.DecimalField(max_digits=10, default=0.00, decimal_places=2)

    # extra = models.JSONField(blank=True, null=True)

    def price_ttc(self):
        return str(self.price * (1 + self.TAX_AMOUNT/100.0))

    def __str__(self):
        return  str(self.cart) + " - " + str(self.product)
