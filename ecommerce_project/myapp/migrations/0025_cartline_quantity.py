# Generated by Django 3.2.7 on 2021-10-10 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_alter_orderline_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartline',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]