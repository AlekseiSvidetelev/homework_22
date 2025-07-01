from catalog.models import Product
from config.settings import CACHE_ENABLED
from django.core.cache import cache


def get_products_cache():
    """Получить список продуктов из кэша или из базы данных"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category(category_id):
    """Получить список продуктов по категории из кэша или из базы данных"""

    cache_key = f"products_by_category_{category_id}"
    products = cache.get(cache_key)
    if products is not None:
        return products
    products = Product.objects.filter(category_id=category_id)
    cache.set(cache_key, products, 60 * 5)
    return products
