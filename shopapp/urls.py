from django.urls import path
from .views import (
    shop_index,
    ShopIndexView,
    group_list,
    GroupsListView,
    product_list,
    ProductDetailView,
    ProductsListView,
    order_detail_view,
    OrderListView,
    OrderDetailView,
    create_product,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    order_create,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
)


app_name = 'shopapp'

urlpatterns = [
    path('', ShopIndexView.as_view(), name='shop_index'),
    path('groups/', GroupsListView.as_view(), name='groups_list'),
    path('products/', ProductsListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/confirm-delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('orders/', OrderListView.as_view(), name='orders_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_details'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order_update'),
    path('orders/<int:pk>/confirm-delete/', OrderDeleteView.as_view(), name='order_delete'),
    path('orders/create/', OrderCreateView.as_view(), name='order_create'),

]