from django.shortcuts import render
from facilities.models import PetHotel
from django.core.exceptions import ValidationError

def show_facilities_page(request):
    facilities = PetHotel.objects.all()
    
    context = {
        'facilities': facilities
    }
    
    
    return render(request, template_name='facilities/facilities_home.html', context = context)

def show_a_facility_page_by_selected_city(request, city):
    facility = PetHotel.objects.get(name = city or None)
    
    if facility:
        context = {
            'facility': facility
        }
    else: 
        raise ValidationError("The facility does not exist!") 
    
    return render(request, template_name='facilities/pet_oasis_city.html', context = context)
    
