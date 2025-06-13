from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, ProductsListView, ProductsDetailView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("catalog/", ProductsListView.as_view(), name="base"),
    path("catalog/product_details/<int:pk>", ProductsDetailView.as_view(), name="product_details"),
    path("catalod/create/", ProductCreateView.as_view(), name="product_create")
]
