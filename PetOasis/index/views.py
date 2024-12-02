from django.shortcuts import render
from accounts.models import Profile

# Create your views here.
def index(request):
    user = Profile.objects.get
    
    context = {
        'user': user
    }
    
    
    return render(request, template_name='index.html', context = context)