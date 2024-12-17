from django import forms
from pets.models import Pet

class RegisterPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ('owner',)
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-group'}),
            'species': forms.Select(attrs={'class': 'form-group'}),
            'breed': forms.TextInput(attrs={'class': 'form-group'}),
            'age': forms.NumberInput(attrs={'class': 'form-group', 'min': 0}),
            'weight': forms.NumberInput(attrs={'class': 'form-group'}),
        }
        
        '''labels = {
            'name': "Name:",
            'species': "Species:",
            'breed': "Breed (optional):",
            'age': "Age:",
            'weight': "Weight (kg): ",
        }'''
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = "My pet's name is..."
        self.fields['species'].widget.attrs['placeholder'] = "My pet's species is..."
        self.fields['breed'].widget.attrs['placeholder'] = "My pet's breed is..."
        self.fields['age'].widget.attrs['placeholder'] = "My pet's age is..."
        self.fields['weight'].widget.attrs['placeholder'] = "My pet weighs..."
     
        
class DeletePetForm(forms.ModelForm):
    
    class Meta:
        model = Pet
        fields = ()