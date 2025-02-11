from audioop import reverse
from lib2to3.fixes.fix_input import context

from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, ListView

from .forms import WalletForm
from .models import Client, ShopItem


class AboutMeView(UserPassesTestMixin, DetailView):
    def test_func(self):
        return self.request.user == self.get_object().user

    template_name = 'market/client.html'
    model = Client
    context_object_name = 'client'


class ClientUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user == self.get_object().user

    model = Client
    fields = 'name'
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse('market:client_info', kwargs={'pk': self.object.pk})


def wallet_up(request:HttpRequest, *args, **kwargs) -> HttpResponse:
    form = WalletForm()
    context = {
        'form': form,
    }

    if request.method == 'POST' and request.user.is_authenticated:
        form = WalletForm(request.POST)
        if form.is_valid():
            client = Client.objects.get(user=request.user)
            add_summ = int(request.POST['balance'])
            client.balance += add_summ
            client.save()
            return HttpResponseRedirect(request.path_info)

    return render(request, 'market/wallet_up.html', context = context)


class ProductsListView(ListView):
    template_name = 'market/products-list.html'
    queryset = ShopItem.objects.all()

class ProductDetailView(DetailView):
    template_name = 'market/product_details.html '
    model = ShopItem
    context_object_name = 'product'