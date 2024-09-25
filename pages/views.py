from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView
from blog.models import Post
from django.http import JsonResponse
from .models import ContactRequest
from .forms import ContactForm, ConsultationForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class ContactRequestCreateView(CreateView):
    model = ContactRequest
    form_class = ContactForm
    template_name = 'contact.html'

    def form_invalid(self, form):
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({'success': True}, status=201)


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['is_about_page'] = True
        return context


class ConsultationRequestView(FormView):
    template_name = 'consultation_form.html'
    form_class = ConsultationForm

    def form_valid(self, form):
        form.save()
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        return JsonResponse({'errors': form.errors}, status=400)