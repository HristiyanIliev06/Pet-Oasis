from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.core.validators import MinValueValidator
from accounts.models import Profile


class CustomUserForm(UserCreationForm):
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
        fields = ('first_name','last_name', 'age', 'username', 'email')
        
        

class CustomUserEditForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):        #MORE REALISTIC DESIGN IF THE TIME ALLOWS IT
        model = get_user_model()
        fields = "__all__"
        
class DeleteAccountForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

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