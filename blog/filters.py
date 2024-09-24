import django_filters
from django import forms
from .models import Post, PostCategory


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        label='Post Title',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by title'}),
        lookup_expr='icontains'
    )

    category = django_filters.ModelChoiceFilter(
        queryset=PostCategory.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Category'
    )

    class Meta:
        model = Post
        fields = ['title', 'category']
