# Generated by Django 3.0.4 on 2020-06-17 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200528_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_discount',
            field=models.BooleanField(default=True),
        ),
    ]