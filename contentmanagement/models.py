from django.db import models


class MainCarouselItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='main_carousel_images/')
    order = models.IntegerField(default=0)  # To manage the display order

    def __str__(self):
        return self.title


class ProductsCarouselItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products_carousel_images/')
    order = models.IntegerField(default=0)  # To manage the display order

    def __str__(self):
        return self.title


class CustomerReview(models.Model):
    customer_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    review_text = models.TextField()
    logo = models.ImageField(upload_to='customer_reviews_logos/', blank=True, null=True)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.customer_name


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question


class ShowcaseCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ShowcaseProduct(models.Model):
    category = models.ForeignKey(ShowcaseCategory, on_delete=models.CASCADE, related_name='showcase_products')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_one = models.ImageField(upload_to='showcase/')
    image_two = models.ImageField(upload_to='showcase/')
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

