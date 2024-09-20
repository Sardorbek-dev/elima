from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('news/', PostListView.as_view(), name='news'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]
