# Generated by Django 3.2.7 on 2021-11-08 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_charactname_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charactname',
            name='charact_desc_id',
        ),
    ]
