from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView
from .models import Post, PostCategory
from .filters import PostFilter
from django.http import JsonResponse


class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    paginate_by = 6 # Display 6 posts initially

    def get_queryset(self):
        queryset = Post.objects.filter(publish=True)

        if self.request.method == 'GET':
            self.filterset = PostFilter(self.request.GET, queryset=queryset)
        else:
            self.filterset = PostFilter(self.request.POST, queryset=queryset)

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        context['post_categories'] = PostCategory.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        offset = int(request.POST.get('offset', 0))
        limit = offset + self.paginate_by

        # Get the current filter parameters
        filterset = PostFilter(request.POST, queryset=self.get_queryset())
        filtered_posts = filterset.qs[offset:limit]

        html = render_to_string(
            'blog/post_items.html',
            {'posts': filtered_posts},
            request=request
        )

        # Check if there are more posts after this batch
        has_more = filterset.qs.count() > limit

        return JsonResponse({
            'html': html,
            'has_more': has_more,
        })


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch other posts excluding the current one
        other_posts = Post.objects.exclude(id=self.object.id).order_by('-created_at')[:3]

        # Add to the context
        context['other_posts'] = other_posts

        return context