from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django_countries.fields import CountryField
from sorl.thumbnail import ImageField

from .managers import CommonUserManager, StaffManager

# Create your models here.

class CustomUser(AbstractUser):
    class GenderChoices(models.IntegerChoices):
        MALE = 1, 'Male'
        FEMALE = 2, 'Female'
        OTHERS = 3, 'Others'

    last_name = None
    first_name = None
    name = models.CharField(verbose_name='Full Name', max_length=100)
    photo = ImageField(upload_to='users', null=True, blank=True)
    dob = models.CharField(max_length=100, null=True, blank=True, verbose_name='Date of Birth')
    gender = models.SmallIntegerField(choices=GenderChoices.choices, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    owner = models.BooleanField(default=False)
    details = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    updated_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')

    def __str__(self):
        return self.email


class Staff(CustomUser):
    class Meta:
        proxy = True

    objects = StaffManager()

    def save(self, *args, **kwargs):
        self.is_staff = True
        super().save(*args, **kwargs)


class CommonUser(CustomUser):
    class Meta:
        proxy = True

    objects = CommonUserManager()


class GroupProfile(models.Model):
    class RoleChoices(models.IntegerChoices):
        STAFF = 1, 'Staff'
        SELLER = 2, 'Seller'

    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    role = models.SmallIntegerField(choices=RoleChoices.choices, null=True, blank=True)
