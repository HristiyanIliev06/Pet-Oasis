from django.db import models
from accounts.models import Profile
from django.core.validators import MinValueValidator

class Pet(models.Model):
    
    SPECIES_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
    ]
    
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,)
    
    species = models.CharField(
        max_length=20,
        choices=SPECIES_CHOICES,
        blank=False,
        null=False,)
    
    breed = models.CharField(
        max_length=100,
        blank=True,
        null=True,)
    
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
        upload_to='profile_pics/pets/',
        blank=True,
        null=True,)
    
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='pets')

    def __str__(self):
        return self.name