# Generated by Django 3.2.7 on 2021-10-18 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_staff_user_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='student',
            new_name='staff',
        ),
    ]
