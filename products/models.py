import uuid

from django.db import models
from django.utils import timezone

from accounts.models import CustomUser
from category.models import Category
from config.models import TimeUnit
from shop.models import Store

# Create your models here.


class ProductModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(delete=True)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    sku = models.CharField(max_length=100, null=True, blank=True)
    upc = models.CharField(max_length=100, null=True, blank=True)
    discount = models.PositiveIntegerField(blank=True, null=True)
    available = models.IntegerField(blank=True, null=True)
    star_rating = models.IntegerField(blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    detail_desc = models.CharField(max_length=150, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    # extra = models.JSONField(blank=True, null=True)
    total_sale = models.IntegerField(blank=True,null=True)
    top_ranked = models.BooleanField(default=False)
    created_by = models.ForeignKey(CustomUser, related_name="product_created_by", on_delete=models.CASCADE, editable=False,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(CustomUser, related_name="product_updated_by", on_delete=models.CASCADE, null=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    delete = models.BooleanField(default=False)
    def formfield_for_foreignkey(self, category, request, **kwargs):
        pass


    objects = ProductModelManager()

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"Name: {self.name}"
    
class ProductPriceModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(delete=True)


class ProductPrice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity_min = models.PositiveIntegerField(default=1)
    quantity_max = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    # time of delivery
    delivery_time = models.IntegerField()
    # unit of time of delivery
    time_unit = models.ForeignKey(TimeUnit, on_delete=models.PROTECT)
    discount_price = models.DecimalField(max_digits=12, null=True, blank=True, decimal_places=2)
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(CustomUser, related_name="p_price_created_by", on_delete=models.CASCADE, editable=False,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(CustomUser, related_name="p_price_updated_by", on_delete=models.CASCADE, null=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    # extra = models.JSONField(blank=True, null=True)

    delete = models.BooleanField(default=False)

    objects = models.Manager()
    buyer_objects = ProductPriceModelManager()

    class Meta:
        verbose_name_plural = 'ProductPrices'


class ProductMediaModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(delete=True)


class ProductMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    media = models.FileField(upload_to="products/")
    display_order = models.PositiveIntegerField(default=0, verbose_name="The position '1' means is the first image(default to display), "
                                                                        "basically all other have the position '0'", db_index=True)
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(CustomUser, related_name="p_media_created_by", on_delete=models.CASCADE, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(CustomUser, related_name="p_media_updated_by", on_delete=models.CASCADE, null=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    # extra = models.JSONField(blank=True, null=True)

    delete = models.BooleanField(default=False)

    objects = ProductMediaModelManager()

    class Meta:
        verbose_name_plural = 'ProductMedias'


class ProductSlider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=900)
    media = models.FileField(upload_to="slider/")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self) -> str:
        return self.title
