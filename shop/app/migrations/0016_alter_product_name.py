# Generated by Django 3.2.7 on 2021-11-01 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, db_index=True, default=None, max_length=200, null=True),
        ),
    ]
