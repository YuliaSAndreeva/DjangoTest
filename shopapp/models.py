from itertools import product

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Product(models.Model):
    class Meta:
        ordering = ['name']
        # db_table = 'new_products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)


    @property
    def description_short(self) -> str:
        if len(self.description) <50:
            return self.description
        return self.description[:50] + '...'

    def __str__(self) -> str:
        return f'Товар {self.name}, pk: {self.pk}'



class Order(models.Model):
    address = models.TextField(null=True, blank=True)
    promo = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name='orders')