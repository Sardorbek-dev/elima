from django.urls import path
from .views import MainCarouselView, ProductsCarouselView

urlpatterns = [
    path('carousel/', MainCarouselView.as_view(), name='main_carousel'),
    path('products-carousel/', ProductsCarouselView.as_view(), name='products_carousel'),
]