from django.contrib import admin
from .models import Post, PostCategory


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # Fields to display in the admin list view
    prepopulated_fields = {'slug': ('name',)}  # Auto-populate slug based on the name


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, CategoryAdmin)