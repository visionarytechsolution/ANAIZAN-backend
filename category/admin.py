from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from category.models import Category, SuggestedCategory

# Register your models here.

admin.site.register(Category, MPTTModelAdmin)
admin.site.register(SuggestedCategory, MPTTModelAdmin)
