from django.db import models
from accounts.models import Profile
from django.core.validators import MaxValueValidator

class News(models.Model):  
    title = models.CharField(
        max_length = 20,
        null = False,
        blank = False               #Might require extending
    )
    
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='blog_posts')
    
    
    description = models.TextField()
    
    image = models.ImageField()
    
    when_uploaded = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title

class OpinionPost(News):
    rating = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(
                5,
                message="We get you've spent a great time with our services but 5 paws in enough for us! Thank you and come back again:)"
                )
        ]
    )
