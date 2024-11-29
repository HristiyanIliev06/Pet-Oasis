from django.db import models
from accounts.models import Profile

class Pet(models.Model):
    
    SPECIES_CHOICES = [
        ('dog', 'dog'),
        ('cat', 'cat'),
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
    
    weight = models.PositiveIntegerField(
        blank=False,
        null=False)
    
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='pets')

    def __str__(self):
        return self.name