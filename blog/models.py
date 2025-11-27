from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from unidecode import unidecode
from django.core.validators import FileExtensionValidator

class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = _("Post Category")
        verbose_name_plural = _("Post Categories")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    slug = models.SlugField(unique=True, blank=True)
    content = RichTextField(config_name='default')
    author = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='img/', blank=True, null=True)
    # video = models.FileField(
    #     upload_to='videos/',
    #     blank=True, null=True,
    #     validators=[FileExtensionValidator(['mp4', 'mov', 'avi'])]
    # )
    created_at = models.DateTimeField(default=timezone.now)
    show_on_homepage = models.BooleanField(default=False)
    publish = models.BooleanField(default=True)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            print("Generating slug for:", self.title)
            self.slug = slugify(unidecode(self.title))
        else: 
            print("Slug already exists or title is missing")
        super().save(*args, **kwargs)
