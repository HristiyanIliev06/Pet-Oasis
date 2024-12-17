from django.shortcuts import render
from facilities.models import PetHotel
from django.core.exceptions import ValidationError
from accounts.models import Profile
from django.contrib.auth.models import AnonymousUser

def show_facilities_page(request):
    facilities = PetHotel.objects.all()
    
    if not isinstance(request.user, AnonymousUser):
        profile = Profile.objects.get(user=request.user)
    else:
        profile = None
    
    context = {
        'facilities': facilities,
        'profile': profile,
    }
    
    
    return render(request, template_name='facilities/facilities_home.html', context = context)

def show_a_facility_page_by_selected_city(request, city:str):
    facility = PetHotel.objects.get(city = city or None)
    
    if not isinstance(request.user, AnonymousUser):
        profile = Profile.objects.get(user=request.user)
    else:
        profile = None
    
    if facility:
        context = {
            'facility': facility,
            'profile': profile,
        }
    else: 
        raise ValidationError("The facility does not exist!") 
    
    return render(request, template_name='facilities/pet_oasis_city.html', context = context)
    
