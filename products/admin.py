from django.contrib import admin

from products.models import Product, ProductMedia, ProductPrice

# Register your models here.


admin.site.register(Product)
admin.site.register(ProductPrice)
admin.site.register(ProductMedia)
