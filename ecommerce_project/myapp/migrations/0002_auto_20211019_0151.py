# Generated by Django 3.2.7 on 2021-10-18 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='address_user_of', to='myapp.address'),
        ),
    ]
