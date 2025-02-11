from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from pyexpat.errors import messages

from .admin_mixins import Export_goods_mixin
from .models import Product, Order

class OrderInLine(admin.TabularInline):
    model = Product.orders.through

@admin.action(description='Безопасное удаление')
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)


@admin.action(description='Восстановление')
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)

@admin.action(description=f'Установить скидку 5%%  для товаров без скидки')
def set_discount_to_5_percent(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.filter(discount=0).update(discount=5)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, Export_goods_mixin):

    actions = [
        mark_archived,
        mark_unarchived,
        'export_csv',
        set_discount_to_5_percent,
    ]

    inlines = [
        OrderInLine,
    ]
    list_display = 'pk', 'name', 'description_short', 'discount', 'archived'
    list_display_links = 'pk', 'name'
    ordering = ['-pk']
    search_fields = ['name', 'description']

    fieldsets = [
        (None, {
            'fields': ('name', 'description'),
        }),
        ('Настройка цены', {
            'fields': ('price', 'discount'),
            'classes': ('collapse',)
        }),
        ('Дополнительные опции:', {
            'fields': ('archived',),
            'classes': ('collapse',),
            'description': 'Безопасное удаление',
        }),
    ]


    def description_short(self, obj: Product) -> str:
        if len(obj.description) <50:
            return obj.description
        return obj.description[:50] + '...'



#class ProductInline(admin.StackedInline):
class ProductInline(admin.TabularInline):
    model = Order.products.through

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    inlines = [
        ProductInline,
    ]

    list_display = 'pk', 'address', 'promo', 'created_at', 'user_name'
    list_display_links = 'pk', 'address'

    def get_queryset(self, request):
        return Order.objects.select_related('user')

    def user_name(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username

#admin.site.register(Product, ProductAdmin)


