from django.contrib import admin
from .models import ContactRequest, ConsultationRequest


class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'created_at']
    search_fields = ['name', 'email', 'phone_number']
    list_filter = ['created_at']


class ConsultationRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'created_at']
    search_fields = ['name', 'phone_number']
    list_filter = ['created_at']


admin.site.register(ContactRequest, ContactRequestAdmin)
admin.site.register(ConsultationRequest, ConsultationRequestAdmin)

