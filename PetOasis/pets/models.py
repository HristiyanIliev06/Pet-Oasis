from django.db import models
from accounts.models import Profile
from django.core.validators import MinValueValidator

class Pet(models.Model):
    
    SPECIES_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
    ]
    
    name = models.CharField(
        max_length=100)
    
    species = models.CharField(
        max_length=20,
        choices=SPECIES_CHOICES)
    
    breed = models.CharField(
        max_length=100)
    
    age = models.PositiveIntegerField(
        blank=False,
        null=False)
    
    weight = models.FloatField(
        blank=False,
        null=False,
        validators = [
            MinValueValidator
            (0,
             message = "It's not possible for your pet to weigh less than 0 kg!",)
            ]
        )
    
    image = models.ImageField(
        upload_to='profile_pics/')
    
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='pets')

    def __str__(self):
        return self.name