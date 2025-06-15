from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Category, Product
from catalog.constants import FORBIDDEN_WORDS


class CategoryForm(ModelForm):
    """Форма для создания категории."""

    class Meta:
        model = Category
        fields = "__all__"


class ProductForm(ModelForm):
    """Форма для создания товара."""

    class Meta:
        model = Product
        exclude = ("views_count",)

    def __init__(self, *args, **kwargs):
        """Функция для задания формы создания товара."""
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Название товара"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Описание товара"}
        )
        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Цена товара"}
        )
        self.fields["category"].widget.attrs.update({"class": "form-control"})
        self.fields["photo"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Размер не должен превышать 5 МБ. Формат файла: .jpg или .png",
            }
        )

    def clean_price(self):
        """Функция для валидации цены товара."""
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError(
                "Стоимость товара не может быть меньше нуля. Пожалуйста, проверьте данные."
            )
        else:
            return price

    def clean(self):
        """Функция для валидации названия и описания товара на предмет запрещенных слов."""
        cleaned_data = super().clean()
        name = cleaned_data.get("name").lower()
        description = cleaned_data.get("description").lower()
        for word in FORBIDDEN_WORDS:
            if word in name or word in description:
                raise ValidationError(
                    f"В названии или описании товара запрещено использовать слово: {word}."
                )

    def clean_photo(self):
        """Функция для валидации изображения товара."""
        photo = self.cleaned_data.get("photo")
        max_size = 5 * 1024 * 1024
        if not photo:
            return photo
        if photo.size > max_size:
            raise ValidationError("Размер изображения не должен превышать 5 МБ.")
        if not photo.name.endswith((".jpg", ".png")):
            raise ValidationError("Формат файла изображения должен быть .jpg или .png.")
        else:
            return photo
