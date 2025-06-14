from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (
    contacts,
    home,
    ProductsListView,
    ProductsDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("catalog/", ProductsListView.as_view(), name="base"),
    path(
        "catalog/product_details/<int:pk>",
        ProductsDetailView.as_view(),
        name="product_details",
    ),
    path("catalog/create", ProductCreateView.as_view(), name="product_create"),
    path("catalog/update/<int:pk>", ProductUpdateView.as_view(), name="product_update"),
    path("catalog/delete/<int:pk>", ProductDeleteView.as_view(), name="product_delete"),
]
