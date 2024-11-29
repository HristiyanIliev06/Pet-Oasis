from django.db import models
from django.core.validators import MinLengthValidator
from validators import pet_hotel_and_shelter_name_validator as phsnv
from pets.models import Pet



class PetHotel(models.Model):
    
    name = models.CharField(
        max_length=20,
        null = False,
        blank = False,
        unique = True,
        validators=[MinLengthValidator(8, message="The pet hotel's name must consist of at least 8 letters!"), 
                    phsnv],)
    
    city = models.CharField(
        max_length=12)
    
    street = models.CharField(
        max_length = 30,
        null = False,
        blank = False,
    )
    
    street_number = models.PositiveSmallIntegerField(
        null = False,
        blank = False,
    )
    
    phone = models.CharField(max_length=15)
    
    email = models.EmailField()
    
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Shelter(PetHotel):
    
    PET_SECTIONS = [
        ('dog', 'dog'),
        ('cat', 'cat'),
    ]
    
    pethotel = models.ForeignKey(                   #Might require extending
        PetHotel,
        on_delete=models.CASCADE,
        related_name='shelters')
    
    pet_section = models.CharField(
        choices=PET_SECTIONS
    )
    
    def __str__(self):
        return f'{self.name}, {self.pethotel.name}' 
    
       
class Booking(models.Model):
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name='bookings'
        )
    
    hotel = models.ForeignKey(
        PetHotel,
        on_delete=models.CASCADE,
        related_name='bookings'
        )
    
    check_in = models.DateField()
    check_out = models.DateField()
    
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pet.name} - {self.hotel.name}"
    


