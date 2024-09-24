from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView
from django.http import JsonResponse

from .filters import ProductFilter
from .models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'store/products.html'
    context_object_name = 'products'
    paginate_by = 8 # Display 8 products initially

    def get_queryset(self):
        """Return available products only, filtered if necessary."""
        queryset = Product.objects.filter(availability=True)

        # Use GET parameters when dealing with filtering
        if self.request.method == 'GET':
            self.filterset = ProductFilter(self.request.GET, queryset=queryset)
        else:  # Handles POST for AJAX
            self.filterset = ProductFilter(self.request.POST, queryset=queryset)

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        context['categories'] = Category.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        offset = int(request.POST.get('offset', 0))
        limit = offset + self.paginate_by

        # Get the current filter parameters
        filterset = ProductFilter(request.POST, queryset=self.get_queryset())
        filtered_products = filterset.qs[offset:limit]

        html = render_to_string(
            'store/product_items.html',
            {'products': filtered_products},
            request=request
        )

        return JsonResponse({
            'html': html,
            'has_more': filtered_products.count() == self.paginate_by,
        })


class ProductDetailView(DetailView):
    model = Product

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        return JsonResponse({
            'name': product.name,
            'description': product.description,
            'size': product.size,
            'price': product.price,
            'min_amount': product.min_amount,
            'material': product.material,
            'warming_material': product.warming_material,
            'filling': product.filling,
            'hood': product.hood,
            'image_url': product.image.url if product.image else '',
        })
