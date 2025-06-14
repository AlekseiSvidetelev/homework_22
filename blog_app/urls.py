from django.urls import path

from blog_app.views import (
    BlogPostsListView,
    BlogPostDetailsView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView,
)
from blog_app.apps import BlogAppConfig

app_name = BlogAppConfig.name

urlpatterns = [
    path("posts/", BlogPostsListView.as_view(), name="blog"),
    path("posts/create/", BlogPostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/", BlogPostDetailsView.as_view(), name="post_details"),
    path("posts/<int:pk>/update/", BlogPostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete/", BlogPostDeleteView.as_view(), name="post_delete"),
]
