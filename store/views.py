import json
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.files.base import ContentFile

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
        categories = Category.objects.all()
        for category in categories:
            print(f"Category ID: {category.id}, Name: {category.name}")
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
            data = json.loads(request.body)
            product_data = data.get('onCrmProductUpdate', {})
            properties = product_data.get('PROPERTIES', {})
            additional_data = product_data.get('ADDITIONAL_DATA', {})
            bitrix_product_id = product_data.get('ID')

            # Utility function to safely get nested dictionary values
            def safe_get(dictionary, *keys):
                for key in keys:
                    if isinstance(dictionary, dict):
                        dictionary = dictionary.get(key, '')
                    else:
                        return ''  # Return empty string if the expected structure is not found
                return dictionary

            # Directly fetching fields from the main `product_data`
            name = safe_get(product_data, 'NAME')
            description = safe_get(properties, 'DESCRIPTION', 'VALUE', 'TEXT')
            price = float(safe_get(properties, 'PRODUCT_PRICE_UZS', 'VALUE') or 0)
            min_amount = int(safe_get(properties, 'MIN_AMOUNT', 'VALUE') or 1)

            # Retrieve Category objects based on provided values
            def get_category_by_id_or_name(value):
                """
                Fetch a Category instance by ID or multi-language name.
                """
                if value.isdigit():  # If the value is a digit, try to find it by ID
                    try:
                        return Category.objects.get(id=value)
                    except Category.DoesNotExist:
                        logger.warning(f"Category with ID '{value}' does not exist.")
                        return None

                # If not a digit, try to find it by multi-language name
                try:
                    return Category.objects.get(
                        Q(name=value) | Q(name_en=value) | Q(name_ru=value) | Q(name_uz=value)
                    )
                except Category.DoesNotExist:
                    logger.warning(f"Category with name '{value}' does not exist in any language.")
                    return None

            # Extract category information in multiple languages
            category = get_category_by_id_or_name(safe_get(properties, 'PRODUCTCATEGORY', 'VALUE')) or Category.objects.first()

            # Multi-language and other fields
            name_en = safe_get(properties, 'NAME_EN', 'VALUE')
            name_ru = safe_get(properties, 'NAME_RU', 'VALUE')
            name_uz = safe_get(properties, 'NAME_UZ', 'VALUE')
            description_en = safe_get(properties, 'DESCRIPTION_EN', 'VALUE', 'TEXT')
            description_ru = safe_get(properties, 'DESCRIPTION_RU', 'VALUE', 'TEXT')
            description_uz = safe_get(properties, 'DESCRIPTION_UZ', 'VALUE', 'TEXT')
            size = safe_get(properties, 'SIZE', 'VALUE')
            size_en = safe_get(properties, 'SIZE_EN', 'VALUE')
            size_ru = safe_get(properties, 'SIZE_RU', 'VALUE')
            size_uz = safe_get(properties, 'SIZE_UZ', 'VALUE')
            material = safe_get(properties, 'MATERIAL', 'VALUE')
            material_en = safe_get(properties, 'MATERIAL_EN', 'VALUE')
            material_ru = safe_get(properties, 'MATERIAL_RU', 'VALUE')
            material_uz = safe_get(properties, 'MATERIAL_UZ', 'VALUE')
            warming_material = safe_get(properties, 'WARMING_MATERIAL', 'VALUE')
            warming_material_en = safe_get(properties, 'WARMING_MATERIAL_EN', 'VALUE')
            warming_material_ru = safe_get(properties, 'WARMING_MATERIAL_RU', 'VALUE')
            warming_material_uz = safe_get(properties, 'WARMING_MATERIAL_UZ', 'VALUE')
            filling = safe_get(properties, 'FILLING', 'VALUE')
            filling_en = safe_get(properties, 'FILLING_EN', 'VALUE')
            filling_ru = safe_get(properties, 'FILLING_RU', 'VALUE')
            filling_uz = safe_get(properties, 'FILLING_UZ', 'VALUE')
            hood = safe_get(properties, 'HOOD', 'VALUE')
            hood_en = safe_get(properties, 'HOOD_EN', 'VALUE')
            hood_ru = safe_get(properties, 'HOOD_RU', 'VALUE')
            hood_uz = safe_get(properties, 'HOOD_UZ', 'VALUE')

            # Create or update the product in your Django app
            product, created = Product.objects.update_or_create(
                bitrix_product_id = bitrix_product_id,  # Using Bitrix ID as unique identifier
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
                    'availability': safe_get(properties, 'AVAILABILITY', 'VALUE') == 'Y',
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


           # Image retrieval and saving
            more_photo_data = safe_get(additional_data, 'PROPERTIES', 'MORE_PHOTO', 'VALUE')
            print('more_photo_data', more_photo_data)
            logger.info(f"Extracted MORE_PHOTO data: {more_photo_data}")

            # Handle both list and dict structures in more_photo_data
            if isinstance(more_photo_data, list) and more_photo_data:
                first_image = more_photo_data[0]
                image_src = safe_get(first_image, 'SRC')
            elif isinstance(more_photo_data, dict):
                image_src = safe_get(more_photo_data, 'SRC')
            else:
                image_src = None

            logger.info(f"Image SRC found: {image_src}")

            if image_src:
                image_url = f"https://elima.space{image_src}"
                print('Attempting to retrieve image from URL', image_url)
                logger.info(f"Attempting to retrieve image from URL: {image_url}")

                # Step 1: Start a session
                session = requests.Session()

                # Step 2: Log in to Bitrix
                login_url = "https://elima.space/bitrix/admin"  # Adjust to your actual login URL
                payload = {
                    'AUTH_FORM': 'Y',
                    'TYPE': 'AUTH',
                    'USER_LOGIN': 'danilapopov2d@gmail.com',  # Adjust to actual username field
                    'USER_PASSWORD': 'SYhLYY7Dzw7E2vx??',  # Adjust to actual password field
                }

                # Define headers (adjust as needed for Bitrix)
                image_headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                    'Referer': 'https://elima.space/bitrix/admin',  # Adjust if needed to point to a relevant page
                    'Accept': 'image/webp,*/*',
                }

                # Authenticate and get the session cookie
                login_response = session.post(login_url, data=payload, headers=image_headers)
                if login_response.status_code == 200:
                    print('Successfully logged in to Bitrix.')
                    logger.info("Successfully logged in to Bitrix.")
                else:
                    logger.error(f"Failed to log in to Bitrix. Status code: {login_response.status_code}")
                    return JsonResponse({'status': 'error', 'message': 'Authentication failed'}, status=500)

                # Fetch the image with session cookie
                image_response = session.get(image_url)
                if image_response.status_code == 200:
                    logger.info("Image retrieved successfully. Saving image...")
                    product.image.save(
                        f"{product.name}_image.jpg",
                        ContentFile(image_response.content),
                        save=True
                    )
                else:
                    logger.error(f"Failed to retrieve image. Status code: {image_response.status_code}")
            else:
                logger.warning("No valid SRC found in the MORE_PHOTO data.")

            return JsonResponse({'status': 'success', 'message': 'Product added successfully'}, status=201)

        except Exception as e:
            logger.error(f"Error processing Bitrix webhook: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
