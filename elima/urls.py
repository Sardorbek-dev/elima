from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns



urlpatterns = [
    path('ckeditor5/', include('ckeditor_uploader.urls')),  # Include CKEditor URLs
    path('i18n/', include('django.conf.urls.i18n')),  # Include i18n URL patterns for language switching
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('blog/', include('blog.urls')),
    path('store/', include('store.urls')),
    path('contentmanagement/', include('contentmanagement.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
