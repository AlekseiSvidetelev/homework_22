from django.urls import reverse_lazy, reverse

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from catalog.models import Product
from catalog.forms import ProductForm


class ProductsListView(ListView):
    """Вывод списка продуктов."""

    model = Product


class ProductsDetailView(DetailView):
    """Вывод детальной информации о продукте."""

    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    """Создание нового продукта."""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:base")


class ProductUpdateView(UpdateView):
    """Изменение существующего продукта."""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:base")

    def get_success_url(self):
        return reverse("catalog:product_details", args={self.kwargs.get("pk")})


class ProductDeleteView(DeleteView):
    """Удаление существующего продукта."""

    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:base")
