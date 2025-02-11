from django import forms
from django.contrib.auth.models import Group
from django.core import validators

from shopapp.models import Product, Order


# class ProductForm(forms.Form):
#     name = forms.CharField(label = 'Название', max_length=100)
#     price = forms.DecimalField(label = 'Цена', max_digits=5, max_value=10000, decimal_places=2)
#     description = forms.CharField(
#         label = 'Описание товара',
#         widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}),
#         validators=[validators.RegexValidator(
#             regex=r'новый',
#             message='Необходимо слово "новый"',
#
#         )],
#     )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'name', 'description', 'discount'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = 'address', 'promo', 'products'

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']