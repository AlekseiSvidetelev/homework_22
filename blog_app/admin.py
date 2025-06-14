from django.contrib import admin

from blog_app.models import Blog


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "content",
        "is_published",
        "creation_date",
        "view_count",
    )
    list_filter = ("is_published",)
    search_fields = ("title", "content")
