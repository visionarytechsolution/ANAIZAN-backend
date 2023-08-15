import uuid

from autoslug import AutoSlugField
from django.core.validators import MaxValueValidator
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField,TreeManager

from accounts.models import CustomUser
from category.utils import create_new_category_code_number

# Create your models here.


class CategoryModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(delete=True)


class Category(MPTTModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=7, default=create_new_category_code_number, unique=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    slug = AutoSlugField(default="", populate_from='name', unique_with=['name', 'code'],)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(CustomUser, related_name="cat_created_by", on_delete=models.CASCADE, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    updated_by = models.ForeignKey(CustomUser, null=True, blank=True, related_name="cat_updated_at", on_delete=models.CASCADE, editable=False)
    category = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, db_index=True, related_name='cat_children')
    delete = models.BooleanField(default=False)

    objects = CategoryModelManager()

    class MPTTMeta:
        parent_attr = "category"
        order_insertion_by = ["name"]

    class Meta:
        unique_together = ('slug', 'name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return f"Name : {self.name} Code : {self.code}"


class CategoryMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    catagory = models.OneToOneField(Category, on_delete=models.CASCADE)
    media = models.FileField(upload_to="category/")
    created_by = models.ForeignKey(CustomUser, related_name="c_media_created_by", on_delete=models.CASCADE, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(CustomUser, related_name="c_media_updated_by", on_delete=models.CASCADE, null=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


class SuggestedCategoryModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(delete=True)


class SuggestedCategory(MPTTModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(CustomUser, related_name="sug_created_by", on_delete=models.CASCADE, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    updated_by = models.ForeignKey(CustomUser, related_name="sug_updated_at", on_delete=models.CASCADE, null=True, blank=True, editable=False)
    category = TreeForeignKey(Category, null=True, blank=True, related_name='sug_children', db_index=True,
                              on_delete=models.CASCADE)

    delete = models.BooleanField(default=False)

    objects = SuggestedCategoryModelManager()

    class MPTTMeta:
        parent_attr = "category"
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = 'Suggested Category'
        verbose_name_plural = 'Suggested Categories'

