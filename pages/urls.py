from django.urls import path
from .views import HomePageView, ContactCreateView, AboutView, ProductsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact', ContactCreateView.as_view(), name='contact'),
    path('about', AboutView.as_view(), name='about'),
    path('products', ProductsView.as_view(), name='products'),
]