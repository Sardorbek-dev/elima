import uuid
from django.db import models


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


class ProductRequest(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='requests')
    full_name_request = models.CharField(max_length=255)
    phone_number_request = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request by {self.full_name_request} for {self.phone_number_request}"