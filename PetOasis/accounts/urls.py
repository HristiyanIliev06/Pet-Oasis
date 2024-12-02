from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('account/', include([
        path('', views.show_account, name = 'show_account'),
        path('register/', views.UserRegisterView.as_view(), name = 'register'),
        path('sign_in/', views.sign_in, name = 'sign_in'),
        #path('sign_out/', views.sign_out, name = 'sign_out'), Not actually
        path('edit/', views.edit_account, name = 'edit_account'),
        path('delete/', views.delete_account, name = 'delete_account'),])),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)