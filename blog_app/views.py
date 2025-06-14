from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from blog_app.models import Blog


# Create your views here.


class BlogPostsListView(ListView):
    model = Blog


class BlogPostDetailsView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogPostCreateView(CreateView):
    model = Blog
    fields = ["title", "content", "preview", "is_published"]
    success_url = reverse_lazy("blog_app:blog")

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogPostUpdateView(UpdateView):
    model = Blog
    fields = ["title", "content", "preview", "is_published"]
    success_url = reverse_lazy("blog_app:blog")

    def get_success_url(self):
        return reverse("blog_app:post_details", args={self.kwargs.get("pk")})


class BlogPostDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog_app:blog")
