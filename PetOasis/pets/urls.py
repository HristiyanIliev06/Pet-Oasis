from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from pets import views

urlpatterns = [
    path(' ', views.PetCreateView.as_view(), name = 'add_pet'),
    path(' ', views.PetDeleteView.as_view(), name = 'delete_pet')
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)