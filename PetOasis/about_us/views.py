from django.shortcuts import render
from accounts.models import Profile
from django.contrib.auth.models import AnonymousUser

def show_about_us_page(request):

    if not isinstance(request.user, AnonymousUser):
        profile = Profile.objects.filter(user=request.user).first()
    else:
        profile = None
    
    context = {
        'profile': profile,
    }
    
    return render(request, 'about_us.html', context)
