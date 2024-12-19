from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from accounts.forms import UserRegisterForm, EditAccountForm, DeleteAccountForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout #, get_user_model
from accounts.models import Profile
from pets.models import Pet


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        # First save the user
        response = super().form_valid(form)
        user = self.object
        
        # Create the associated profile
        Profile.objects.create(
            user=user,
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            age=form.cleaned_data['age']
        )
        
        # Log the user in
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        
        return response


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')
    
    def get_success_url(self):
        return self.success_url

#@login_required
def show_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    pets = Pet.objects.filter(owner=user.profile)
    
    context = {
        'user': user,
        'profile': profile,
        'pets': pets,
    }
    
    return render(request, 'accounts/show_profile.html', context)


class UserEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = EditAccountForm
    template_name = 'accounts/edit_account.html'
    success_url = reverse_lazy('show_profile')
    
    def get_object(self, queryset=None):
        return self.request.user.profile
    
    def form_valid(self, form):
        user = self.request.user
        profile = self.get_object()
        
        # Update user fields
        user.username = form.cleaned_data['username']
        user.email = form.cleaned_data['email']
        
        # Change password if provided
        new_password = form.cleaned_data.get('new_password')
        if new_password:
            user.set_password(new_password)
        
        user.save()
        profile.save()
        
        return super().form_valid(form)


class DeleteAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/delete_account.html'
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        form = DeleteAccountForm(initial={'username': request.user.username})
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = DeleteAccountForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password == confirm_password:
                user = authenticate(username=request.user.username, password=password)
                if user is not None and user == request.user:
                    # Profile will be deleted automatically due to CASCADE
                    logout(request)
                    user.delete()
                    return redirect(self.success_url)
                else:
                    form.add_error('password', "Invalid password.")
            else:
                form.add_error('confirm_password', "Passwords do not match.")
        
        return self.render_to_response({'form': form})
