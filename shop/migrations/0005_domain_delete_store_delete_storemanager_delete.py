# Generated by Django 4.1.1 on 2022-10-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_store_logo_alter_store_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='store',
            name='delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='storemanager',
            name='delete',
            field=models.BooleanField(default=False),
        ),
    ]
