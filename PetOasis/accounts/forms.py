from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import MinValueValidator

from accounts.models import Profile

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'My first name is...'})
    )
    
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'My last name is...'})
    )
    
    age = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(18, message="Sorry! You are not mature enough to use our pet services!")],
        initial=18
    )
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'age', 'password1', 'password2')
        
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'I prefer that you call me...'}),
            'email': forms.EmailInput(attrs={'placeholder': 'My email is...'}),
        }
        
        labels = {
            'username': "Username:",
            'email': "Email:",
            'first_name': "First name:",
            'last_name': "Last name:",
            'age': "Age:",
            'password1': 'Password:',
            'password2': 'Confirm password:'
        }


class EditAccountForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    old_password = forms.CharField(widget=forms.PasswordInput, required=True)
    new_password = forms.CharField(widget=forms.PasswordInput, required=False)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput, required=False)
    
    class Meta:
        model = Profile
        fields = ['username', 'email', 'old_password',
                  'account_picture', 'new_password',
                  'confirm_new_password']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['username'].initial = self.instance.user.username
            self.fields['email'].initial = self.instance.user.email
            
    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_new_password = cleaned_data.get('confirm_new_password')
        
        if new_password and new_password != confirm_new_password:
            raise forms.ValidationError("New passwords do not match.")
            
        return cleaned_data
        
    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.user.check_password(old_password):
            raise forms.ValidationError("Incorrect password.")
        return old_password


class DeleteAccountForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=True
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your current password'}),
        required=True
    )
    
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
        required=True
    )
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
            
        return cleaned_data