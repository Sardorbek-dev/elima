# forms.py
from django import forms
from .models import ProductRequest


class ProductRequestForm(forms.ModelForm):
    class Meta:
        model = ProductRequest
        fields = ['full_name_request', 'phone_number_request']
