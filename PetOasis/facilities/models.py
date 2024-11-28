from django.db import models
from django.core.validators import MinLengthValidator
from validators import pet_hotel_and_shelter_name_validator as phsnv


class PetHotel(models.Model):
    
    name = models.CharField(
        max_length=20,
        null = False,
        blank = False,
        unique = True,
        validators=[MinLengthValidator(8, message="The pet hotel's name must consist of at least 8 letters!"), 
                    phsnv],)
    
    
    street = models.CharField(
        max_length = 30,
        null = False,
        blank = False,
    )
    
    street_number = models.PositiveSmallIntegerField(
        null = False,
        blank = False,
    )
    
    description = models.TextField()

class Shelter(models.Model):
    
    PET_SECTIONS = [
        ('dog', 'dog'),
        ('cat', 'cat')
    ]
    
    pethotel = models.ForeignKey(                   #Might require extending
        PetHotel,
        on_delete=models.CASCADE,
        related_name='shelters')
    
    pet_section = models.CharField(
        choices=PET_SECTIONS
    )
    
