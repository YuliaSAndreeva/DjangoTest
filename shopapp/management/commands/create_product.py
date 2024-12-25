from django.core.management import BaseCommand

from shopapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Создание продукта')
        products = [
            'телефон',
            'планшет',
            'колонка',
        ]
        for product in products:
            new_product, created = Product.objects.get_or_create(name=product)
            if created:
                self.stdout.write(f'Продукт {new_product.name} создан')
        self.stdout.write('Продукты создан')