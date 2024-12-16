from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Pet
from .forms import RegisterPetForm, DeletePetForm

class PetCreateView(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = RegisterPetForm
    template_name = 'pets/pet_form.html'
    success_url = reverse_lazy('show_profile')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class PetDeleteView(LoginRequiredMixin, DeleteView):
    model = Pet
    form_class = DeletePetForm
    template_name = 'pets/pet_confirm_delete.html'
    success_url = reverse_lazy('show_profile')
