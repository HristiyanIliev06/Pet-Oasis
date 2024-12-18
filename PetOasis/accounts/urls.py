from django.urls import path, reverse_lazy
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.show_profile, name = 'show_profile'),
    path('register/', views.UserRegisterView.as_view(), name = 'register'),
    path('login/', views.CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'), #NEEDS ALTERATIONS!!!
    path('edit/', views.UserEditView.as_view(), name = 'edit_profile'),
    path('delete/', views.DeleteAccountView.as_view(), name = 'delete_account'),
]