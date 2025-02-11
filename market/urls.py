from django.urls import path, include

from market import views

app_name = 'market'



urlpatterns = [
    path('client/<int:pk>/', views.AboutMeView.as_view(), name='client_info'),
    path('client/<int:pk>/update/', views.ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/wallet_up/', views.wallet_up, name='wallet_up'),
    path('products/', views.ProductsListView.as_view(), name='products'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_details'),

]