# Generated by Django 3.2.7 on 2021-11-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_productinbasket_nmb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
