# Generated by Django 3.2.7 on 2021-10-31 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20211031_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinbasket',
            name='nmb',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
