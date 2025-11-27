from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin
from modeltranslation.forms import TranslationModelForm

from .models import Category, Product, ProductRequest

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')

class ProductRequestAdmin(admin.ModelAdmin):
    list_display = ('product', 'full_name_request', 'phone_number_request', 'created_at')
    list_filter = ('product', 'created_at')
    search_fields = ('full_name_request', 'phone_number_request')




class ProductAdmin(TranslationAdmin):
    # 🔥 ВАЖНО: говорим админке, что для всех RichTextUploadingField нужен CKEditor
    formfield_overrides = {
        RichTextUploadingField: {'widget': CKEditorUploadingWidget},
    }

    list_display = ('name', 'category', 'price', 'availability')
    list_filter = ('category', 'availability')
    search_fields = ('name',)

    # TranslationAdmin сам развернёт это в name_ru/name_en/... и т.п.
    fields = ('name', 'short_content', 'description', 'availability' )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductRequest, ProductRequestAdmin)

