from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_field = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

class StatusAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class OrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder


admin.site.register(ProductInOrder, ProductInOrderAdmin)


class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]

    class Meta:
        model = ProductInBasket


admin.site.register(ProductInBasket, ProductInBasketAdmin)


class CharactNameAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CharactName._meta.fields]

    class Meta:
        model = CharactName


admin.site.register(CharactName, CharactNameAdmin)


class CharactDescAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CharactDesc._meta.fields]

    class Meta:
        model = CharactDesc


admin.site.register(CharactDesc, CharactDescAdmin)


class ProfileAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]

    class Meta:
        model = Profile

admin.site.register(Profile, ProfileAdmin)