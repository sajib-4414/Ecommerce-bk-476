# Generated by Django 3.2.7 on 2021-10-18 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20211019_0151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='buyer',
            new_name='admin',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='seller',
            new_name='staff',
        ),
    ]
