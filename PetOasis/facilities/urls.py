from django.urls import path
from facilities import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(' ', views.show_facilities_page, name = 'facilities'),
    path('<str:city>', views.show_a_facility_page_by_selected_city, name = 'facility'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)