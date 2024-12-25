from django.http import HttpResponse,HttpRequest
from django.shortcuts import render
from timeit import default_timer as timer

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