from itertools import product
from lib2to3.fixes.fix_input import context

from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from timeit import default_timer as timer

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from shopapp.form import ProductForm, OrderForm, GroupForm
from shopapp.models import Product, Order

class ShopIndexView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
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


class GroupsListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'form': GroupForm(),
            'groups': Group.objects.prefetch_related('permissions').all(),

        }
        return render(request, 'shopapp/group_list.html', context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.path)


def product_list(request: HttpRequest):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'shopapp/product_list.html', context = context)


class ProductsListView(ListView):
    template_name = 'shopapp/product_list.html'
    # model = Product
    queryset = Product.objects.filter(archived=False)
    context_object_name = 'products'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['products'] = Product.objects.all()
    #     return context

# class ProductsDetailView(View):
#
#     def get(self, request: HttpRequest, pk: int) -> HttpResponse:
#         #product = Product.objects.get(pk=pk)
#         product = get_object_or_404(Product, pk=pk)
#         context = {
#             'product': product,
#         }
#         return render(request, 'shopapp/products_detail.html ', context = context)


class ProductDetailView(DetailView):
    template_name = 'shopapp/products_detail.html '
    model = Product
    context_object_name = 'product'


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
    return render(request, 'shopapp/product_form.html', context = context)


class ProductCreateView(CreateView):
    model = Product
    fields = 'name', 'price', 'description', 'discount'
    # form_class = ProductForm
    success_url = reverse_lazy('shopapp:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = 'name', 'price', 'description', 'discount'
    template_name_suffix = '_update'

    def get_success_url(self):
        return reverse(
            'shopapp:product_detail',
            kwargs={'pk': self.object.pk}
        )


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('shopapp:product_list')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


def order_detail_view(request: HttpRequest):

    context = {
        'orders' : Order.objects.select_related('user').prefetch_related('products').all(),
    }
    return render(request, 'shopapp/order_list.html', context = context)


class OrderListView(ListView):
    # model = Order

    queryset = (
        Order.objects
        .select_related('user')
        .prefetch_related('products')
    )


class OrderDetailView(DetailView):
    queryset = (
        Order.objects
        .select_related('user')
        .prefetch_related('products')
    )



def order_create(request: HttpRequest):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        url = reverse("shopapp:orders_list")
        return redirect(url)

    form = OrderForm()

    context = {
        'form': form,
    }
    return render(request, 'shopapp/order_create.html', context = context)