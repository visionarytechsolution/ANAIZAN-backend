from django.db import models


class StaffManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_staff=True)


class CommonUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_staff=False)