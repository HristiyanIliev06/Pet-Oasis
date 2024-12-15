from django.core.exceptions import ValidationError

def pet_hotel_and_shelter_name_validator(value:str):
    if not value.isalpha():
        raise ValidationError("The pet hotel's name may consist of letters only!")
    
    if ' ' not in value:
        raise ValidationError("The pet hotel's name must contain at least one space!")
    
    mandatory_condition1, mandatory_condition2, city = value.split(' ')
    
    if mandatory_condition1!='Pet' or mandatory_condition2!='Oasis':
        raise ValidationError("The first word of the pet hotel's name must be after the hotel chain 'Pet Oasis'!")
    
    if city[0].islower():
        raise ValidationError("Cities' names are always written with a starting capital letter!")