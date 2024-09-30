from django.views.generic import TemplateView


class MainCarouselView(TemplateView):
    template_name = 'contentmanagement/main-carousel.html'


class ProductsCarouselView(TemplateView):
    template_name = 'contentmanagement/products-carousel.html'


class PostsCarouselView(TemplateView):
    template_name = 'contentmanagement/posts-carousel.html'


class CustomerReviewsCarouselView(TemplateView):
    template_name = 'contentmanagement/customer-reviews-carousel.html'


class FAQView(TemplateView):
    template_name = 'contentmanagement/frequently-asked-questions.html'


class ShowcaseProductView(TemplateView):
    template_name = 'contentmanagement/showcase-carousel.html'