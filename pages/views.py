from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Post


class HomePageView(TemplateView):
    template_name = 'home.html'


class ContactCreateView(TemplateView):
    template_name = 'contact.html'


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['is_about_page'] = True
        return context


class ProductsView(TemplateView):
    template_name = 'products.html'
