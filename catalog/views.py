from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Product


class ProductsListView(ListView):
    model = Product


class ProductsDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "description", "price", "photo", "category"]
    success_url = reverse_lazy("catalog:base")


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


# def products_list(request):
#     catalog = Product.objects.all()
#     context = {"catalog": catalog}
#     return render(request, "product_list.html", context)


# def products_details(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, "product_detail.html", context)
