from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'posts.html'  # Specify your template
    context_object_name = 'posts'  # Custom context variable
    ordering = ['-created_at']  # Order by most recent


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'
    context_object_name = 'post'