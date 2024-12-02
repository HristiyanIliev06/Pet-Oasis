from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import CustomUserForm

# Create your views here.
class UserRegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')

def sign_in(request):
    pass

#def sign_out(request):     Not actually
#    pass

def show_account(request):
    pass

def edit_account(request):
    pass

def delete_account(request):
    pass