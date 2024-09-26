from django.urls import path
from .views import MainCarouselView, ProductsCarouselView, PostsCarouselView, CustomerReviewsCarouselView, FAQView, ShowcaseProductView

urlpatterns = [
    path('carousel/', MainCarouselView.as_view(), name='main_carousel'),
    path('products-carousel/', ProductsCarouselView.as_view(), name='products_carousel'),
    path('posts-carousel/', PostsCarouselView.as_view(), name='posts_carousel'),
    path('customer-reviews-carousel/', CustomerReviewsCarouselView.as_view(), name='customer_reviews_carousel'),
    path('faqs/', FAQView.as_view(), name='faqs'),
    path('showcase/', ShowcaseProductView.as_view(), name='showcase'),
]