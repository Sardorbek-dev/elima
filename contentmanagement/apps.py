from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ContentmanagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contentmanagement'
    verbose_name = _("Управление контентом") 
