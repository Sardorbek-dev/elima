from django.views.generic import TemplateView, CreateView, FormView
from django.http import JsonResponse

from contentmanagement.models import MainCarouselItem, ProductsCarouselItem, CustomerReview, FAQ, ShowcaseProduct, ShowcaseCategory, History
from blog.models import Post
from .models import ContactRequest
from .forms import ContactForm, ConsultationForm


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_carousel_items'] = MainCarouselItem.objects.all().order_by('order')
        context['products_carousel_items'] = ProductsCarouselItem.objects.all().order_by('order')
        context['posts'] = Post.objects.filter(show_on_homepage=True)
        context['reviews'] = CustomerReview.objects.filter(publish=True)
        context['faqs'] = FAQ.objects.filter(is_active=True)
        context['historys'] = History.objects.filter()

        # Add rating range for each review
        for review in context['reviews']:
            review.rating_range = list(range(review.rating))

        return context


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
        context['is_about_page'] = True
        context['showcase_categories'] = ShowcaseCategory.objects.all()
        context['showcase_products'] = ShowcaseProduct.objects.filter(publish=True)
        return context


class ConsultationRequestView(FormView):
    template_name = 'consultation_form.html'
    form_class = ConsultationForm

    def form_valid(self, form):
        form.save()
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        return JsonResponse({'errors': form.errors}, status=400)


class Custom404View(TemplateView):
    template_name = 'page_not_found.html'
