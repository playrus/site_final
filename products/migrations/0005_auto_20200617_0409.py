# Generated by Django 3.0.4 on 2020-06-17 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200617_0406'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Категория товара', 'verbose_name_plural': 'Категории товаров'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='shourt_description',
        ),
    ]
