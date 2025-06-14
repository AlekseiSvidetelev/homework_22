from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    preview = models.ImageField(
        upload_to="images/", verbose_name="Превью", blank=True, null=True
    )
    creation_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикации"
    )
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    view_count = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
