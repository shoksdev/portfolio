# Generated by Django 4.2 on 2023-05-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_supplier_address_alter_supplier_city_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['product_id']},
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название товара'),
        ),
    ]
