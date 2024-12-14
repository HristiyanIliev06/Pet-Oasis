from django.db import models
from accounts.models import Profile
from django.core.validators import MaxValueValidator

class PawPost(models.Model): 
     
    title = models.CharField(
        max_length = 20,
        null = False,
        blank = False               #Might require extending
    )
    
    description = models.TextField()
    
    image = models.ImageField(upload_to='profile_pics/pawposts/')
    
    when_uploaded = models.DateTimeField(auto_now_add=True)
    
    additional_mentions = models.CharField(
        null=True,
        blank=True,
    )
    
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True,
        related_name='pawposts')
    
    
    def __str__(self):
        return self.title
