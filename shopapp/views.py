from django.contrib.auth.models import Group
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

def group_list(request: HttpRequest):
    context = {
        'groups': Group.objects.prefetch_related('permissions').all(),

    }
    return render(request, 'shopapp/group_list.html', context = context)