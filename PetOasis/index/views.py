from django.shortcuts import render
from blog_and_news.models import PawPost
from facilities.models import PetHotel


# Create your views here.
def index(request):
    current_user = request.user
    
    top_3_facilities = PetHotel.objects.filter(id__lte=3)
    
    pawposts = PawPost.objects.all()
    
    context = {
        'user': current_user,
        'profile': current_user.profile,
        'top_3_facilities': top_3_facilities,
        'pawposts': pawposts,
        
    }
    
    
    return render(request, template_name='index.html', context = context)