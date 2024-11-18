from django.urls import path, include
from accounts import views

urlpatterns = [
    path('account/', include([
        path('', views.show_account, name = 'show_account'),
        path('sign_up/', views.sign_up, name = 'sign_up'),
        path('sign_in/', views.sign_in, name = 'sign_in'),
        #path('sign_out/', views.sign_out, name = 'sign_out'), Not actually
        path('edit/', views.edit_account, name = 'edit_account'),
        path('delete/', views.delete_account, name = 'delete_account'),])),
]
