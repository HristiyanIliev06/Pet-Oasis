from django import forms
from blog_and_news.models import PawPost


class PawPostForm(forms.ModelForm):
    class Meta:
        model = PawPost
        fields = ['title', 'image', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-select'}),
            'image': forms.ImageField(attrs={'class': 'form-image'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    