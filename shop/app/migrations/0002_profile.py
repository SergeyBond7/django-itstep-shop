# Generated by Django 3.2.7 on 2021-10-29 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=64, verbose_name='Имя')),
                ('lastname', models.CharField(default='', max_length=64, verbose_name='Фамилия')),
                ('phone', models.CharField(blank=True, default='', max_length=64, verbose_name='Телефон')),
                ('avatar', models.ImageField(blank=True, default='profile_avatars/default.jpg', upload_to='profile_avatars/%Y/%m/%d', verbose_name='Аватар')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
