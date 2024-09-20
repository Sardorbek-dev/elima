from django.urls import path
from .views import HomePageView, ContactCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact', ContactCreateView.as_view(), name='contact'),
]