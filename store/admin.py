from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin
from modeltranslation.forms import TranslationModelForm

from .models import Category, Product, ProductRequest, Services, Cases, ProductImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')

class ProductRequestAdmin(admin.ModelAdmin):
    list_display = ('product', 'full_name_request', 'phone_number_request', 'created_at')
    list_filter = ('product', 'created_at')
    search_fields = ('full_name_request', 'phone_number_request')

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

class CasesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1          # сколько пустых строк показывать по умолчанию
    fields = ("image", "alt_text", "ordering",)
    verbose_name = "Доп. фото"
    verbose_name_plural = "Галерея товара"


class ProductAdmin(TranslationAdmin):
    # 🔥 ВАЖНО: говорим админке, что для всех RichTextUploadingField нужен CKEditor
    formfield_overrides = {
        RichTextUploadingField: {'widget': CKEditorUploadingWidget},
    }

    list_display = ('name', 'category', 'availability')
    list_filter = ('category', 'availability')
    search_fields = ('name',)

    fields = ('name', 'short_content', 'description', 'category', 'image', 'availability' )
    inlines = [ProductImageInline]



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductRequest, ProductRequestAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Cases, CasesAdmin)

