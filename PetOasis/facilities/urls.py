from django.urls import path, include
from facilities import views

urlpatterns = [
    path('facilities/', include([
        path('<city:slug>', views.show_a_facility_page_by_selected_city, name = 'facility')])),
]
