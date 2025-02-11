from django.contrib import admin

from market.models import Client, ShopItem, Shop, Product


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name'
    list_display_links = 'pk', 'name'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name'
    list_display_links = 'pk', 'name'


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name'
    list_display_links = 'pk', 'name'

@admin.register(ShopItem)
class ShopItemAdmin(admin.ModelAdmin):
    list_display = 'pk', 'product'
    list_display_links = 'pk', 'product'