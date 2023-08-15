# Generated by Django 4.1.1 on 2022-10-28 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0013_alter_cart_user_alter_cartitem_cart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='cart_item', to='carts.cart'),
        ),
    ]
