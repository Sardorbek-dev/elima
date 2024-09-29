from django.contrib import admin
from .models import Category, Product, ProductRequest


class ProductRequestAdmin(admin.ModelAdmin):
    list_display = ('product', 'full_name_request', 'phone_number_request', 'created_at')
    list_filter = ('product', 'created_at')
    search_fields = ('full_name_request', 'phone_number_request')


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductRequest, ProductRequestAdmin)

