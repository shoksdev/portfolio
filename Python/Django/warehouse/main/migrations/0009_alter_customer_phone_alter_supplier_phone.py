# Generated by Django 4.2 on 2023-05-15 10:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_customer_phone_alter_supplier_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, default='Не заполнено', max_length=16, null=True, unique=True, validators=[django.core.validators.RegexValidator(regex='^((8|\\+7)[\\- ]?)?(\\(?\\d{3}\\)?[\\- ]?)?[\\d\\- ]{7,10}$')]),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone',
            field=models.CharField(blank=True, default='Не заполнено', max_length=16, null=True, unique=True, validators=[django.core.validators.RegexValidator(regex='^((8|\\+7)[\\- ]?)?(\\(?\\d{3}\\)?[\\- ]?)?[\\d\\- ]{7,10}$')]),
        ),
    ]
