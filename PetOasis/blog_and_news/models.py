from django.db import models
from accounts.models import Profile
from django.core.validators import MaxValueValidator

class BlogAndNewsAbstractModel(models.Model): 
    
    class Meta:
        abstract = True
         
    title = models.CharField(
        max_length = 20,
        null = False,
        blank = False               #Might require extending
    )
    
    description = models.TextField()
    
    image = models.ImageField(upload_to='profile_pics/')
    
    when_uploaded = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
class News(BlogAndNewsAbstractModel):
    
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True,
        related_name='news')

class PawPost(BlogAndNewsAbstractModel):
    #Just a kind of post for opinions, thoughts and reviews:)
    
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True,
        related_name='pawposts')
    
    rating = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(
                5,
                message="We get you've spent a great time with our services but 5 paws in enough for us! Thank you and come back again:)"
                )
        ]
    )
