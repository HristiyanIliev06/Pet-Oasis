from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from pets.models import Pet
from accounts.forms import UserRegisterForm, EditAccountForm, DeleteAccountForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, logout, get_user_model

'''from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages'''


#profile = Profile.objects.get(user=request.user) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# @login_required !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class UserRegisterView(CreateView):
    model = get_user_model()
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

class CustomLoginView(LoginView):
    fields = '__all__'
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')


def show_profile(request):
    pets = Pet.objects.filter(owner = request.user)
    
    context = {
        'user': request.user,
        'pets': pets,
    }
    
    return render(request, 'accounts/show_profile.html', context)

class UserEditView(LoginRequiredMixin, UpdateView):
    form_class = EditAccountForm
    template_name = 'accounts/edit_account.html'
    success_url = reverse_lazy('show_profile')
    
def delete_account(request):
    pass

class DeleteAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/delete_account.html'
    success_url = reverse_lazy('index')

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
    
