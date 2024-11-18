from django.urls import path
from blog_and_news import views

urlpatterns = [
    path('blog-and-news/', views.show_blog_and_news_page, name = 'blog_and_news'),
]
