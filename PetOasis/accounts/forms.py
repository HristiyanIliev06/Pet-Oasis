from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.core.validators import MinValueValidator
from accounts.models import Profile

"""class ProfileForm(forms.Form):
    user_form = CombinedUserUpdateForm()
    profile_form = UserProfileUpdateForm()"""
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required = True
    )
    
    last_name = forms.CharField(
        max_length=30,
        required = True,
    )
    
    age = forms.IntegerField(
        required = True,
        validators=[MinValueValidator(18,
        message="Sorry! You are not mature enough to use our pet services!")]
    )
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        
        fields = '__all__'
        
        widgets = {
            'email': forms.EmailInput(),
            'age': forms.NumberInput(),
        }
        
        labels = {
            'first_name': "First name:",
            'last_name': "Last name:",
            'age': "Age:",
            'username': "Username:",
            'email': "Email:",
            'password1': 'Password:',
            'password2': 'Confirm password:'
        }  
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['first_name'].widget.attrs['placeholder'] = 'My first name is...'
        self.fields['last_name'].widget.attrs['placeholder'] = 'My last name is...'
        self.fields['username'].widget.attrs['placeholder'] = 'I prefer that you call me...'
        self.fields['email'].widget.attrs['placeholder'] = 'My email is...'
        self.fields['age'].initial = 18
        
        

class EditAccountForm(UserChangeForm):
    new_password = forms.CharField(
        widget=forms.PasswordInput,
        required=True)
    
    confirm_new_password = forms.CharField(
        widget=forms.PasswordInput,
        required=True)
    
    class Meta(UserChangeForm.Meta):        #MORE REALISTIC DESIGN IF THE TIME ALLOWS IT
        model = get_user_model()
        
        fields = ('username', 'email', 'password',
                  'new_password', 'confirm_new_password')
        
        widgets = {
            'email': forms.EmailInput(),
        }
        
        labels = {
            'username': "New username:",
            'email': "new email:",
            'password': 'Old password:',
            'new_password': 'New password:',
            'confirm_new_password': 'Confirm new password:'
            }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.initial = field
        
            
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        new_password = cleaned_data.get("new_password")
        confirm_new_password = cleaned_data.get("confirm_new_password")
        username = cleaned_data.get("username")

        if new_password != confirm_new_password:
            raise forms.ValidationError("New passwords do not match.")

        # Check if the provided username and password match the logged-in user
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("Incorrect username or password.")
        
        return cleaned_data    
        
        
        
class DeleteAccountForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm your password'}),
        required=True)

    labels = {
            'username': "Username:",
            'password': 'Password:',
            'confirm_password': 'Confirm password:'
            }
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'confirm_password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['disabled'] = 'disabled'
        self.fields['username'].widget.attrs['readonly'] = 'readonly'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter your current password'

        
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        username = cleaned_data.get("username")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        # Check if the provided username and password match the logged-in user
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("Incorrect username or password.")
        
        return cleaned_data