from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='img/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
