from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.show_account, name = 'show_account'),
    path('register/', views.UserRegisterView.as_view(), name = 'register'),
    path('login/', views.CustomLoginView.as_view(), name = 'sign_in'),
     path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('edit/', views.edit_account, name = 'edit_account'),
    path('delete/', views.delete_account, name = 'delete_account'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)