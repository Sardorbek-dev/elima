from django.urls import path
from .views import HomePageView, ContactRequestCreateView, AboutView, ConsultationRequestView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact', ContactRequestCreateView.as_view(), name='contact'),
    path('about', AboutView.as_view(), name='about'),
    path('consultation', ConsultationRequestView.as_view(), name='consultation'),
]