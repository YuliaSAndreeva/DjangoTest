from itertools import product

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Product(models.Model):
    """
    Модель для представления товара,
    который можно продавать в интернет-магазине.
    Заказы: :model: 'shopapp.Order'
    """
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)


    @property
    def description_short(self) -> str:
        if len(self.description) <50:
            return self.description
        return self.description[:50] + '...'

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.name

class ShopItem(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT, related_name='shops')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='цена')
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Имя клиента')
    balance = models.PositiveIntegerField(default=0, verbose_name='Баланс')
    status = models.PositiveIntegerField(default=0, verbose_name='Статус')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name

