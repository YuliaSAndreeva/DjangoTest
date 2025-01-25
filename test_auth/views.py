from audioop import reverse

from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy


def login_view(request:HttpRequest):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/admin/')
        return render(request, 'test_auth/login.html')


    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('/admin/')

    return render(request, 'test_auth/login.html', {'error': 'Invalid username or password'})


def logout_view(request:HttpRequest):
    logout(request)
    return redirect(reverse('test_auth:login'))


class TestLogoutView(LogoutView):
    next_page = reverse_lazy('test_auth:login')


def set_cookie_view(request:HttpRequest) -> HttpResponse:
    response = HttpResponse('Cookie set')
    response.set_cookie('new', 'info', max_age=3600)
    return response


def get_cookie_view(request:HttpRequest) -> HttpResponse:
    value = request.COOKIES.get('new', 'default info')
    return HttpResponse(f'Cookie value: {value}')


def set_session_view(request:HttpRequest) -> HttpResponse:
    request.session['new'] = 'new info'
    return HttpResponse('Session set')


def get_session_view(request:HttpRequest) -> HttpResponse:
    value = request.session.get('new', 'default info')
    return HttpResponse(f'Session value: {value}')

