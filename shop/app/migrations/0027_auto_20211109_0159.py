# Generated by Django 3.2.7 on 2021-11-08 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_profileedit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='', max_length=64, verbose_name='Город'),
        ),
        migrations.DeleteModel(
            name='ProfileEdit',
        ),
    ]
