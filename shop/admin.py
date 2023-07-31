from django.contrib import admin

from shop.models import Domain, Store, StoreManager

# Register your models here.

admin.site.register(Domain)
admin.site.register(Store)
admin.site.register(StoreManager)
