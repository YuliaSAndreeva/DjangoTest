from itertools import product
from lib2to3.fixes.fix_input import context

from django.contrib.auth.models import Group
from django.http import HttpResponse,HttpRequest
from django.shortcuts import render, redirect, reverse
from timeit import default_timer as timer

from shopapp.form import ProductForm, OrderForm
from shopapp.models import Product, Order


def shop_index(request):

    products = [
        ('телефон', '1000'),
        ('планшет', '2000'),
        ('колонкаа', '500'),
    ]


    context = {
        'time_running': timer(),
        'products': products,
    }

    return render(request, 'shopapp/index.html', context=context)

def group_list(request: HttpRequest):
    context = {
        'groups': Group.objects.prefetch_related('permissions').all(),

    }
    return render(request, 'shopapp/group_list.html', context = context)

def product_list(request: HttpRequest):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'shopapp/product_list.html', context = context)

def create_product(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():

           form.save()

        url = reverse("shopapp:product_list")
        return redirect(url)

    form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, 'shopapp/create_product.html', context = context)

def order_detail_view(request: HttpRequest):

    context = {
        'orders' : Order.objects.select_related('user').prefetch_related('products').all(),
    }
    return render(request, 'shopapp/order_detail_view.html', context = context)


def order_create(request: HttpRequest):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        url = reverse("shopapp:order_detail")
        return redirect(url)

    form = OrderForm()

    context = {
        'form': form,
    }
    return render(request, 'shopapp/order_create.html', context = context)