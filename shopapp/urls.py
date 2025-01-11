from django.urls import path
from .views import shop_index, group_list, product_list, order_detail_view, create_product, order_create

app_name = 'shopapp'

urlpatterns = [
    path('', shop_index, name='shop_index'),
    path('groups/', group_list, name='groups_list'),
    path('products/', product_list, name='product_list'),
    path('products/create/', create_product, name='product_create'),
    path('orders/', order_detail_view, name='order_detail'),
    path('orders/create/', order_create, name='order_create'),

]