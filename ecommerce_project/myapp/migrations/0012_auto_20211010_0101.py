# Generated by Django 3.2.7 on 2021-10-09 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20211010_0056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_lines',
        ),
        migrations.AddField(
            model_name='cartline',
            name='cart',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.cart'),
        ),
    ]
