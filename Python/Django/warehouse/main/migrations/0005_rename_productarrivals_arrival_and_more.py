# Generated by Django 4.2 on 2023-05-14 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_product_options_alter_product_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductArrivals',
            new_name='Arrival',
        ),
        migrations.RenameModel(
            old_name='ProductExpenses',
            new_name='Expense',
        ),
    ]
