from django.contrib.auth import get_user_model
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
        
        

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = "__all__"