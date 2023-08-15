from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from config.models import AzPackage


@receiver(post_save, sender=AzPackage)
def custom_package_post_save(sender, created, instance, **kwargs):
    """ This send verification email """
    if created:
        Group.objects.create(name=instance.package_name)

