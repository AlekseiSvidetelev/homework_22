from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductsListView,
    ProductsDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductsListView.as_view(), name="base"),
    path(
        "product_details/<int:pk>", ProductsDetailView.as_view(), name="product_details"
    ),
    path("create", ProductCreateView.as_view(), name="product_create"),
    path("update/<int:pk>", ProductUpdateView.as_view(), name="product_update"),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="product_delete"),
]
