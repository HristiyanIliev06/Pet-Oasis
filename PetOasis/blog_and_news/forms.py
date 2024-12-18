'''from django import forms
from blog_and_news.models import PawPost


class PawPostForm(forms.ModelForm):
    class Meta:
        model = PawPost
        fields = ['title', 'image', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-select'}),
            'image': forms.ImageField(),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    #attrs={'class': 'form-image'}'''