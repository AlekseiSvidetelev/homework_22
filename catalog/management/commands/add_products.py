from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add test categories and catalog to the database."

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        categories = [
            {"name": "Электроника", "description": ""},
            {"name": "Книги", "description": ""},
            {"name": "Одежда", "description": ""},
            {"name": "Спортивные товары", "description": ""},
        ]

        for category_data in categories:
            category, created = Category.objects.get_or_create(**category_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added category: {category.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Category already exists: {category.name}")
                )

        products = [
            {
                "name": "Galaxy S24 Ultra",
                "description": "Флагманский смартфон.",
                "category": Category.objects.get(name="Электроника"),
                "price": 120000.00,
            },
            {
                "name": 'Книга "Искусство программирования"',
                "description": "Классический учебник по информатике.",
                "category": Category.objects.get(name="Книги"),
                "price": 500.00,
            },
            {
                "name": "Футболка Nike",
                "description": "Удобная спортивная одежда.",
                "category": Category.objects.get(name="Одежда"),
                "price": 2000.00,
            },
            {
                "name": "Баскетбольный мяч Adidas",
                "description": "Профессиональный спортивный инвентарь.",
                "category": Category.objects.get(name="Спортивные товары"),
                "price": 1500.00,
            },
        ]

        for prod_data in products:
            product, created = Product.objects.get_or_create(**prod_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added product: {product.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Product  already exists: {product.name}")
                )
