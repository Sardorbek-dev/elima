from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Contact Request")
        verbose_name_plural = _("Contact Requests")

    def __str__(self):
        return self.name


class ConsultationRequest(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    reason = models.CharField(max_length=400, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Consultation Request")
        verbose_name_plural = _("Consultation Requests")

    def __str__(self):
        return f"{self.name} - {self.phone_number}"
