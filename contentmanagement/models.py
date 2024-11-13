from django.db import models
from django.utils.translation import gettext_lazy as _


class MainCarouselItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='main_carousel_images/')
    order = models.IntegerField(default=0)  # To manage the display order

    class Meta:
        verbose_name = _("Main Carousel Item")
        verbose_name_plural = _("Main Carousel Items")

    def __str__(self):
        return self.title


class ProductsCarouselItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products_carousel_images/')
    order = models.IntegerField(default=0)  # To manage the display order

    class Meta:
        verbose_name = _("Products Carousel Item")
        verbose_name_plural = _("Products Carousel Items")

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

    class Meta:
        verbose_name = _("Customer Review")
        verbose_name_plural = _("Customer Reviews")

    def __str__(self):
        return self.customer_name


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")

    def __str__(self):
        return self.question


class ShowcaseCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Showcase Category")
        verbose_name_plural = _("Showcase Categories")

    def __str__(self):
        return self.name


class ShowcaseProduct(models.Model):
    category = models.ForeignKey(ShowcaseCategory, on_delete=models.CASCADE, related_name='showcase_products')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_one = models.ImageField(upload_to='showcase/')
    image_two = models.ImageField(upload_to='showcase/')
    publish = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Showcase Product")
        verbose_name_plural = _("Showcase Products")

    def __str__(self):
        return self.title
