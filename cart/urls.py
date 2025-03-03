from django.urls import path, include

from cart import views

app_name = 'cart'


urlpatterns = [
    path('product/<int:pk>/add/', views.cart_add, name='cart_add'),
    path('product/<int:pk>/delete/', views.cart_delete, name='cart_remove'),
    path('details/', views.cart_details, name='cart_details'),
    path('buy/', views.cart_buy, name='cart_buy'),
]