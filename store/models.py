import uuid
from django.db import models
from modeltranslation.translator import register, TranslationOptions


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    min_amount = models.PositiveIntegerField()
    material = models.CharField(max_length=100)
    warming_material = models.CharField(max_length=100)
    filling = models.CharField(max_length=100)
    hood = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products_images/', blank=True, null=True)

    def __str__(self):
        return self.name
