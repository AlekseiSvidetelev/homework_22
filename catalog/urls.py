from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, products_list, products_details

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("products/", products_list, name="base"),
    path("products/product_details/<int:pk>", products_details, name="product_details"),
]
