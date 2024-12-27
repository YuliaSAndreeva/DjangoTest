from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shopapp.models import Product, Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Создание заказа')
        agent = User.objects.get(username='admin')
        order, _ = Order.objects.get_or_create(
            address = 'Горького,1',
            promo = 'sale',
            user = agent,
        )
        self.stdout.write(f'Заказ {order} создан')