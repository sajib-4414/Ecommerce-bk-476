# Generated by Django 3.2.7 on 2021-10-10 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_company_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
