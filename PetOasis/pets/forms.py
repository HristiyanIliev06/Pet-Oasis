from django import forms
from pets.models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'age']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'species': forms.Select(attrs={'class': 'form-select'}),
            'breed': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }