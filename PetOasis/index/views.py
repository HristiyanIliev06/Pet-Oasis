from django.shortcuts import render
from django.contrib.auth import get_user_model
from accounts.models import Profile

# Create your views here.
def index(request):
    '''UserModel = get_user_model()
    user = UserModel.objects.get()
    
    context = {
        'user': user
    }'''
    
    
    return render(request, template_name='index.html') #, context = context)