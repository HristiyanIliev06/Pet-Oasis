from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog_and_news import views

urlpatterns = [
    path('', views.show_blog_and_news_page, name = 'blog_and_news'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)