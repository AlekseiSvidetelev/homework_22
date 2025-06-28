from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from catalog.models import Product
from catalog.forms import ProductForm, ProductModeratorForm


class ProductsListView(ListView):
    """Вывод списка продуктов."""

    model = Product


class ProductsDetailView(LoginRequiredMixin, DetailView):
    """Вывод детальной информации о продукте."""

    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Создание нового продукта."""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:base")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Изменение существующего продукта."""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:base")

    def get_success_url(self):
        return reverse("catalog:product_details", args={self.kwargs.get("pk")})

    def get_form_class(self):
        """ Изменение формы в зависимости от прав пользователя."""
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("can_unpublish_product") and user.has_perm("can_delete_product"):
            return ProductModeratorForm
        raise PermissionDenied

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление существующего продукта."""

    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:base")

    def has_permission(self, request):
        if request.user == self.object.owner:
            return True
        elif request.user.has_perm("can_delete_product"):
            return True
        else:
            raise PermissionDenied
