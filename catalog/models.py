from django.db import models

from users.models import User


class Category(models.Model):
    """Категория товара"""

    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        permissions = [
            ("can_edit_category", "Может редактировать категории"),
            ("can_delete_category", "Может удалять категории"),
            ("can_add_category", "Может добавлять категории"),
        ]

    def __str__(self):
        return self.name


class Product(models.Model):
    """Товар"""

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    photo = models.ImageField(
        upload_to="catalog/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="catalog",
        verbose_name="Категория",
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена за покупку"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )
    views_count = models.PositiveIntegerField(
        help_text="Укажите количество просмотров",
        default=0,
        verbose_name="Количество просмотров",
    )
    is_published = models.BooleanField(default=False, verbose_name="Опубликован")
    owner = models.ForeignKey(
        User, verbose_name="Владелец", on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "price"]
        permissions = [
            ("can_unpublish_product", "Может снимать продукт с публикации"),
            ("can_delete_product", "Может удалять продукты"),
        ]

    def __str__(self):
        """Возвращает наименование товара"""
        return self.name
