from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from .models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'store/products.html'
    context_object_name = 'products'
    paginate_by = 5  # Display 5 products initially

    def get_queryset(self):
        """Return available products only."""
        return Product.objects.filter(availability=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['grouped_products'] = self.group_products_into_groups(context['products'])
        return context

    def post(self, request, *args, **kwargs):
        offset = int(request.POST.get('offset', 0))
        limit = offset + self.paginate_by
        products = self.get_queryset()[offset:limit]  # Reuse the `get_queryset` method

        grouped_products = self.group_products_into_groups(products)

        return JsonResponse({
            'html': render_to_string('store/product_items.html', {'grouped_products': grouped_products}, request=request),
            'has_more': products.count() == self.paginate_by,
        })

    def group_products_into_groups(self, products):
        """Group products into groups of 5."""
        return [products[i:i + 5] for i in range(0, len(products), 5)]


class ProductDetailView(DetailView):
    model = Product

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        return JsonResponse({
            'name': product.name,
            'description': product.description,
            'size': product.size,
            'price': product.price,
            'min_volume': product.min_volume,
            'material': product.material,
            'warming_material': product.warming_material,
            'filling': product.filling,
            'hood': product.hood,
            'image_url': product.image.url if product.image else '',
        })
