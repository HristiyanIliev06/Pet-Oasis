from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import  PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

from accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    username = models.CharField(
        max_length=100,
        unique=True,
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = AppUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email



class Profile(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    first_name = models.CharField(
        max_length=30,
        null = False,
        blank=False
    )

    last_name = models.CharField(
        max_length=30, 
        null = False,
        blank=False
    )

    age = models.IntegerField(
        null = False,
        blank=False,
        validators=[MinValueValidator(18,
        message="Sorry! You are not mature enough to use our pet services!")]
    )
    
    account_picture = models.ImageField(
        upload_to='profile_pics/profiles/',
        null = True,
        blank=True
        )

#c7qnmfw884398ajjed009hj0854789hj