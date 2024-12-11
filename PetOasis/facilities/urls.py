from django.urls import path, include
from facilities import views

urlpatterns = [
    path(' ', views.show_facilities_page, name = 'facilities'),
    path('<slug:city>', views.show_a_facility_page_by_selected_city, name = 'facility'),
]
