from django.urls import path
from .views import MainCarouselView, ProductsCarouselView, PostsCarouselView

urlpatterns = [
    path('carousel/', MainCarouselView.as_view(), name='main_carousel'),
    path('products-carousel/', ProductsCarouselView.as_view(), name='products_carousel'),
    path('posts-carousel/', PostsCarouselView.as_view(), name='posts_carousel'),
]