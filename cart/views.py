from audioop import reverse

from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from cart.forms import CartAddProductForm
from cart.models import Cart
from market.models import ShopItem, Client


@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    product = get_object_or_404(ShopItem, pk=pk)
    shop = product.shop

    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data

        cart.add(
            product=product,
            shop=shop,
            quantity=cd['quantity'],
            update_quantity=cd['update'],
        )

    return redirect('cart:cart_details')


def cart_delete(request, pk):
    cart = Cart(request)
    product = get_object_or_404(ShopItem, pk=pk)
    cart.remove(product)
    return redirect('cart:cart_details')


def cart_details(request):
    cart = Cart(request)
    return render(request, 'market/cart_details.html', context={'cart': cart})


def cart_buy(request):
    cart = Cart(request)
    for item in cart:
        shopitem = get_object_or_404(ShopItem, id=item['product'].id)
        shopitem.quantity -= item['quantity']
        shopitem.save()

    client = Client.objects.get(user=request.user)
    cart_sum = cart.get_total_sum()
    client.balance -=cart_sum
    client.status += cart_sum
    client.save()

    cart.clear()

    return redirect(reverse('market:client_info', kwargs={'pk': client.pk}))
