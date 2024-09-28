import django_filters
from django import forms
from store.models import Product, Category


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        label='Product Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by name'}),
        lookup_expr='icontains'
    )

    # Add min_price and max_price filters
    min_price = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte', label='Min Price',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Min price'})
    )
    max_price = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte', label='Max Price',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Max price'})
    )

    ordering = django_filters.ChoiceFilter(
        label='Sort by',
        choices=(('asc', 'Ascending'), ('desc', 'Descending')),
        method='filter_by_order'
    )

    category = django_filters.ModelChoiceFilter(
        label='Category',
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    size = django_filters.CharFilter(
        label='Size',
        widget=forms.Select(attrs={'class': 'form-control'}),
        method='filter_by_size',
    )

    def filter_by_size(self, queryset, name, value):
        if value:
            return queryset.filter(size__icontains=value)  # Check if the selected size is part of the size string
        return queryset

    def filter_by_price(self, queryset, name, value):
        # Retrieve min_price and max_price from the request data
        min_price = self.data.get('min_price')
        max_price = self.data.get('max_price')

        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        return queryset

    def filter_by_order(self, queryset, name, value):
        if value == 'asc':
            return queryset.order_by('price')
        elif value == 'desc':
            return queryset.order_by('-price')
        return queryset

    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'size']
