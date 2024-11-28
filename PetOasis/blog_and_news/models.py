from django.db import models

class Post(models.Model):
    title = models.CharField(
        max_length = 20,
        null = False,
        blank = False               #Might require extending
    )
    
    description = models.TextField()
    
    image = models.ImageField()


