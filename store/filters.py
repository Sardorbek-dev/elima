import django_filters
from django import forms
from store.models import Product, Category


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by name'}),
        lookup_expr='icontains'
    )

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
        method='filter_by_size',
    )

    def filter_by_size(self, queryset, name, value):
        if value:
            # Properly filter by size; ensure value is in the comma-separated field
            return queryset.filter(size__icontains=value)
        return queryset

    def filter_by_price(self, queryset, name, value):
        min_price = self.data.get('min_price')
        max_price = self.data.get('max_price')

        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        elif min_price:
            queryset = queryset.filter(price__gte=min_price)
        elif max_price:
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
        fields = ['name', 'min_price', 'max_price', 'category', 'size']
