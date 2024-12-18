from django.urls import path, include

from pets import views

urlpatterns = [
    path('register/', views.PetCreateView.as_view(), name = 'add_pet'),
    path('<int:pk>', include([
        path('delete/', views.PetDeleteView.as_view(), name = 'delete_pet')])),
]




