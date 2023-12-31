# Generated by Django 4.1.1 on 2022-10-26 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='created_by',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='address_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='address',
            name='updated_by',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='address_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
