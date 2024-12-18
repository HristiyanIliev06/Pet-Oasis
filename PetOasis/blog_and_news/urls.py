from django.urls import path
from blog_and_news import views

urlpatterns = [
    
    path('', views.show_blog_and_news_page, name = 'blog_and_news'),
    #path('', views.PawPostCreateView.as_view(), name = 'pawpost_create'),
]



