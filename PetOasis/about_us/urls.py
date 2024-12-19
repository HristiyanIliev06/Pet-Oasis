from django.urls import path
from about_us import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.show_about_us_page, name = 'about_us'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)