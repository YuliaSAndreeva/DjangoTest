from django.urls import path
from .views import shop_index, group_list, product_list, order_detail_view

app_name = 'shopapp'

urlpatterns = [
    path('', shop_index, name='shop_index'),
    path('groups/', group_list, name='groups_list'),
    path('products/', product_list, name='product_list'),
    path('orders/', order_detail_view, name='order_detail'),

]