from django.urls import path
from .views import ProductListView, ProductDetailView, ProductRequestCreateView, BitrixProductWebhookView, \
    ProductDetailPageView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/', ProductDetailPageView.as_view(), name='product_detail_view'),
    path('product-request/', ProductRequestCreateView.as_view(), name='product_request'),
    path('api/bitrix-product/', BitrixProductWebhookView.as_view(), name='bitrix_product_webhook'),
]
