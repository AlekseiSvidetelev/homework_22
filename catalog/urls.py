from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductsListView,
    ProductsDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    CategoryProductsView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductsListView.as_view(), name="base"),
    path(
        "product_details/<int:pk>",
        cache_page(60)(ProductsDetailView.as_view()),
        name="product_details",
    ),
    path("create", ProductCreateView.as_view(), name="product_create"),
    path("update/<int:pk>", ProductUpdateView.as_view(), name="product_update"),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="product_delete"),
    path(
        "category_list/<int:category_id>",
        cache_page(60)(CategoryProductsView.as_view()),
        name="category_list",
    ),
]
