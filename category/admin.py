from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from category.models import Category, SuggestedCategory,CategoryMedia

# Register your models here.

admin.site.register(Category, MPTTModelAdmin)
admin.site.register(SuggestedCategory, MPTTModelAdmin)
admin.site.register(CategoryMedia)
