from django.shortcuts import render
from blog_and_news.models import PawPost
from facilities.models import PetHotel
from accounts.models import Profile
from django.contrib.auth.models import AnonymousUser


# Create your views here.

def index(request):
    current_user = request.user
    
    if not isinstance(request.user, AnonymousUser):
        profile = Profile.objects.get(user=request.user)
    else:
        profile = None
    
    top_3_facilities = PetHotel.objects.all()[0:3]   #filter(id__lte=3)
    
    pawposts = PawPost.objects.all()
    
    context = {
        'user': current_user,
        'profile': profile,
        'top_3_facilities': top_3_facilities,
        'pawposts': pawposts,
        
    }
    
    
    return render(request, template_name='index.html', context = context)