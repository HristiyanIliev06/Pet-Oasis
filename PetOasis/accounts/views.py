from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import CustomUserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model


'''from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages'''

class UserRegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'


#def sign_out(request):     Not actually
#    pass

def show_account(request):
    user = get_user_model()

def edit_account(request):
    pass

def delete_account(request):
    pass