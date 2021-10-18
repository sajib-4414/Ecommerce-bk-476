# Generated by Django 3.2.7 on 2021-10-18 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20211019_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='address_user_of', to='myapp.address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photoIdNum',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]