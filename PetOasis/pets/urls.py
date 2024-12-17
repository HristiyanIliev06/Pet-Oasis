from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from pets import views

urlpatterns = [
    path('register/', views.PetCreateView.as_view(), name = 'add_pet'),
    path('<int:pk>', include([
        path('delete/', views.PetDeleteView.as_view(), name = 'delete_pet')])),
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)