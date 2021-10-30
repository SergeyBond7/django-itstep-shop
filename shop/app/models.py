from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:product_list_by_category',
                        args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:product_detail',
                        args=[self.id, self.slug])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    firstname = models.CharField(max_length=64, default='', verbose_name='Имя')
    lastname = models.CharField(max_length=64, default='', verbose_name='Фамилия')
    phone = models.CharField(blank=True, max_length=64, default='', verbose_name='Телефон')
    avatar = models.ImageField(blank=True, upload_to='profile_avatars/%Y/%m/%d', verbose_name='Аватар',
                               default='profile_avatars/default.jpg')

    def __str__(self):
        return f"{self.user.firstname} {self.user.lastname}"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'