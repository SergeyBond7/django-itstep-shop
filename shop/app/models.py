from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, null=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, null=True)


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
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, db_index=True, null=True, default=None)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return '%s, %s' % (self.price, self.name)

    def get_absolute_url(self):
        return reverse('app:product_detail',
                        args=[self.id, self.slug])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', primary_key=True)
    city = models.CharField(max_length=64, default='', verbose_name='Город',null=True)
    phone = models.CharField(blank=True, max_length=64, default='', verbose_name='Телефон',null=True)
    avatar = models.ImageField(blank=True, upload_to='profile_avatars/%Y/%m/%d', verbose_name='Аватар',
                               default='profile_avatars/default.jpg')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):

        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = int(self.nmb) * price_per_item
        print(self.total_price)

        super(ProductInOrder, self).save(*args, **kwargs)


class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, default=None)
    product = models.ForeignKey(Product,on_delete=models.CASCADE, blank=True, null=True, default=None)
    nmb = models.IntegerField(null=True, blank=True, default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.product.name


    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'


    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = int(self.nmb) * price_per_item

        super(ProductInBasket, self).save(*args, **kwargs)


class CharactName(models.Model):

    category = models.ForeignKey(Category, related_name='characts', on_delete=models.CASCADE, default=None,null=True)
    name1 = models.CharField(max_length=200, db_index=True, null=True, default=None)
    name2 = models.CharField(max_length=200, db_index=True, null=True, default=None)
    name3 = models.CharField(max_length=200, db_index=True, null=True, default=None)
    name4 = models.CharField(max_length=200, db_index=True, null=True, default=None)
    name5 = models.CharField(max_length=200, db_index=True, null=True, default=None)
    product_id = models.ForeignKey(Product, related_name='characts_name', null=True, on_delete=models.CASCADE)


class CharactDesc(models.Model):
    charact_id = models.ForeignKey(CharactName, related_name='characts_desc', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, related_name='characts_desc',null=True, on_delete=models.CASCADE)
    desc1 = models.CharField(max_length=200, db_index=True, null=True, default=None)
    desc2 = models.CharField(max_length=200, db_index=True, null=True, default=None)
    desc3 = models.CharField(max_length=200, db_index=True, null=True, default=None)
    desc4 = models.CharField(max_length=200, db_index=True, null=True, default=None)
    desc5 = models.CharField(max_length=200, db_index=True, null=True, default=None)

    def __str__(self):
        return str(self.charact_id)






