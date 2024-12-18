from django.urls import path
from about_us import views

urlpatterns = [
    path('', views.show_about_us_page, name = 'about_us'),
]

