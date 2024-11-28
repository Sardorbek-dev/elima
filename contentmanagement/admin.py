from django.contrib import admin
from .models import MainCarouselItem, ProductsCarouselItem, CustomerReview, FAQ, ShowcaseCategory, ShowcaseProduct, History


class MainCarouselItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title', 'description')


class ProductsCarouselItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title', 'description')


class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'company_name', 'position', 'rating')
    search_fields = ('customer_name', 'company_name')


class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_active')
    search_fields = ('question',)
    list_filter = ('is_active',)


class ShowcaseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ShowcaseProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publish')

class HistoryAdmin(admin.ModelAdmin):
    list_display = ("text", "statistic")


admin.site.register(MainCarouselItem, MainCarouselItemAdmin)
admin.site.register(ProductsCarouselItem, ProductsCarouselItemAdmin)
admin.site.register(CustomerReview, CustomerReviewAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(ShowcaseCategory, ShowcaseCategoryAdmin)
admin.site.register(ShowcaseProduct, ShowcaseProductAdmin)
admin.site.register(History, HistoryAdmin)


