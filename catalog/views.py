from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from catalog.models import Product


class ProductsListView(ListView):
    model = Product


class ProductsDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "description", "price", "photo", "category"]
    success_url = reverse_lazy("catalog:base")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name", "description", "price", "photo", "category"]
    success_url = reverse_lazy("catalog:base")

    def get_success_url(self):
        return reverse("catalog:product_details", args={self.kwargs.get("pk")})


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:base")


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")
