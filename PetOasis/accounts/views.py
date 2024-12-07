from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from accounts.forms import CustomUserForm, CustomUserEditForm, DeleteAccountForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, logout


'''from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages'''

class UserRegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')


class ShowProfileView(TemplateView):
    template_name = 'accounts/show_profile.html'

class UserEditView(UpdateView):
    form_class = CustomUserEditForm
    template_name = 'accounts/edit_account.html'
    success_url = reverse_lazy('index')
    
def delete_account(request):
    pass

class DeleteAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'users/delete_account.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        # Show the form to the user for confirmation
        form = DeleteAccountForm()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = DeleteAccountForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user is not None and user == request.user:
                # Logout the user and delete the account
                logout(request)
                user.delete()
                return redirect(self.success_url)
            else:
                form.add_error(None, "Invalid credentials. Please check your username and password.")
        
        return self.render_to_response({'form': form})
    
