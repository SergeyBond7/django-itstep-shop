# Generated by Django 3.2.7 on 2021-11-07 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20211107_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charactname',
            name='charact_desc_id',
        ),
    ]