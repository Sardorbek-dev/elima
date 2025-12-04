import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Product(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    bitrix_product_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    short_content = models.TextField(
        verbose_name=_("Short content"),
        blank=True,
        null=True,
        help_text=_("Краткое описание для карточки товара")
    )

    description = RichTextUploadingField(
        verbose_name=_("Description"),
        blank=True,
        null=True,
        help_text=_("Полное описание с картинками и форматированием")
    )

    size = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    min_amount = models.PositiveIntegerField(blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)
    warming_material = models.CharField(max_length=100, blank=True, null=True)
    filling = models.CharField(max_length=100, blank=True, null=True)
    hood = models.CharField(max_length=100, blank=True, null=True)
    availability = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    image = models.ImageField(upload_to='products_images/', blank=True, null=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    """Дополнительные изображения товара"""

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name=_("Product"),
    )
    image = models.ImageField(
        upload_to="products_images/gallery/",
        verbose_name=_("Image"),
    )
    alt_text = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Alt text"),
        help_text=_("Текст для SEO и доступности"),
    )
    ordering = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Ordering"),
        help_text=_("Порядок показа в галерее"),
    )

    class Meta:
        verbose_name = _("Product image")
        verbose_name_plural = _("Product images")
        ordering = ["ordering", "id"]

    def __str__(self):
        return f"{self.product.name} #{self.pk}"

class ProductRequest(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='requests')
    full_name_request = models.CharField(max_length=255)
    phone_number_request = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Product Request")
        verbose_name_plural = _("Product Requests")

    def __str__(self):
        return f"Request by {self.full_name_request} for {self.phone_number_request}"

class Services(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    availability = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Услуги")
        verbose_name_plural = _("Услуги")

class Cases(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='cases/', blank=True, null=True)
    availability = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Кейсы")
        verbose_name_plural = _("Кейсы")
