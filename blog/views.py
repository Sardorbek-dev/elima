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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch other posts excluding the current one
        other_posts = Post.objects.exclude(id=self.object.id).order_by('-created_at')[:3]

        # Add to the context
        context['other_posts'] = other_posts

        return context