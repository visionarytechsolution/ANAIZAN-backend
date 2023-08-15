import uuid

from autoslug import AutoSlugField
from django.contrib.auth.models import Group
from django.db import models
from django.db.models import Q

from accounts.models import CustomUser
from config.models import AzPackage

# Create your models here.

class DomainModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(delete=True)


class Domain(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField(unique=True)
    delete = models.BooleanField(default=False)

    objects = DomainModelManager()

    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = "Domains"

    def __str__(self):
        return "Domain -> " + str(self.url)


class StoreModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(delete=True)


def store_upload_to(instance, filename):
    return f'store_logo/{instance.name}/{filename}'


class Store(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='name', unique_with='name')
    logo = models.ImageField(upload_to=store_upload_to)
    domains = models.ManyToManyField(Domain)
    owner = models.ForeignKey(CustomUser, default='', on_delete=models.PROTECT)
    is_active = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)

    objects = StoreModelManager()

    class Meta:
        verbose_name = "Store"
        verbose_name_plural = "Stores"

    def __str__(self):
        return "Store -> " + str(self.name)


class StoreManagerModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(delete=True)


class StoreManager(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    domains = models.ForeignKey(Domain, on_delete=models.PROTECT)
    role = models.ForeignKey(Group, related_name="store_manager_role", on_delete=models.PROTECT)
    store = models.ManyToManyField(Store)
    delete = models.BooleanField(default=False)

    objects = StoreManagerModelManager()

    class Meta:
        verbose_name = "Store Manager"
        verbose_name_plural = "Store Managers"

    def __str__(self):
        return "Store Manger -> " + str(self.user)
