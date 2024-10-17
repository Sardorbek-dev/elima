import json
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import logging
import requests
import uuid

from .filters import ProductFilter
from .forms import ProductRequestForm
from .models import Product, Category, ProductRequest

logger = logging.getLogger(__name__)

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


class ProductRequestCreateView(CreateView):
    model = ProductRequest
    form_class = ProductRequestForm

    def form_valid(self, form):
        product_id = self.request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        form.instance.product = product
        return super().form_valid(form)

    def form_invalid(self, form):
        return JsonResponse({"errors": form.errors}, status=400)

    def get_success_url(self):
        return reverse_lazy('product_list')

@method_decorator(csrf_exempt, name='dispatch')
class BitrixProductWebhookView(View):
    def post(self, request, *args, **kwargs):
        try:
            logger.info(request.body)
            data = json.loads(request.body)
            product_data = data.get('fields', {})

            # Required fields
            name = product_data.get('NAME')
            description = product_data.get('DESCRIPTION', '')
            price = product_data.get('PRICE', 0)
            category_id = product_data.get('SECTION_ID', '')  # Adjust based on actual Bitrix24 payload

            # Additional fields (including multi-language support)
            size = product_data.get('SIZE', '')
            material = product_data.get('MATERIAL', '')
            warming_material = product_data.get('WARMING_MATERIAL', '')
            filling = product_data.get('FILLING', '')
            hood = product_data.get('HOOD', '')
            min_amount = product_data.get('MIN_AMOUNT', 1)
            availability = product_data.get('AVAILABILITY', True)
            image_url = product_data.get('IMAGE', None)

            # Multi-language fields (assuming Bitrix24 payload supports these fields)
            name_en = product_data.get('NAME_EN', None)
            name_ru = product_data.get('NAME_RU', None)
            name_uz = product_data.get('NAME_UZ', None)
            description_en = product_data.get('DESCRIPTION_EN', None)
            description_ru = product_data.get('DESCRIPTION_RU', None)
            description_uz = product_data.get('DESCRIPTION_UZ', None)
            size_en = product_data.get('SIZE_EN', None)
            size_ru = product_data.get('SIZE_RU', None)
            size_uz = product_data.get('SIZE_UZ', None)
            material_en = product_data.get('MATERIAL_EN', None)
            material_ru = product_data.get('MATERIAL_RU', None)
            material_uz = product_data.get('MATERIAL_UZ', None)
            warming_material_en = product_data.get('WARMING_MATERIAL_EN', None)
            warming_material_ru = product_data.get('WARMING_MATERIAL_RU', None)
            warming_material_uz = product_data.get('WARMING_MATERIAL_UZ', None)
            filling_en = product_data.get('FILLING_EN', None)
            filling_ru = product_data.get('FILLING_RU', None)
            filling_uz = product_data.get('FILLING_UZ', None)
            hood_en = product_data.get('HOOD_EN', None)
            hood_ru = product_data.get('HOOD_RU', None)
            hood_uz = product_data.get('HOOD_UZ', None)

            # Get or create the category
            category = get_object_or_404(Category, id=category_id)

            # Create or update the product in your Django app
            product, created = Product.objects.update_or_create(
                unique_id=product_data.get('ID', uuid.uuid4()),  # Using Bitrix24 ID as unique identifier
                defaults={
                    'name': name,
                    'description': description,
                    'price': price,
                    'size': size,
                    'material': material,
                    'warming_material': warming_material,
                    'filling': filling,
                    'hood': hood,
                    'min_amount': min_amount,
                    'availability': availability,
                    'category': category,

                    # Multi-language fields
                    'name_en': name_en,
                    'name_ru': name_ru,
                    'name_uz': name_uz,
                    'description_en': description_en,
                    'description_ru': description_ru,
                    'description_uz': description_uz,
                    'size_en': size_en,
                    'size_ru': size_ru,
                    'size_uz': size_uz,
                    'material_en': material_en,
                    'material_ru': material_ru,
                    'material_uz': material_uz,
                    'warming_material_en': warming_material_en,
                    'warming_material_ru': warming_material_ru,
                    'warming_material_uz': warming_material_uz,
                    'filling_en': filling_en,
                    'filling_ru': filling_ru,
                    'filling_uz': filling_uz,
                    'hood_en': hood_en,
                    'hood_ru': hood_ru,
                    'hood_uz': hood_uz,
                }
            )

            # If the image URL is provided, download and save it
            if image_url:
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    product.image.save(
                        f'{product.name}_image.jpg',
                        ContentFile(image_response.content),
                        save=True
                    )

            return JsonResponse({'status': 'success', 'message': 'Product added successfully'}, status=201)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)