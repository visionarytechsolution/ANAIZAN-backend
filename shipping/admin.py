from django.contrib import admin

from shipping.models import Address, Shipping

# Register your models here.

admin.site.register(Address)
admin.site.register(Shipping)

