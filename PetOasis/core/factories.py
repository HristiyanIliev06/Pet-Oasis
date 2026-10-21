"""Helpers that build model instances for the tests of every app."""
import itertools

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from accounts.models import Profile
from facilities.models import PetHotel
from pets.models import Pet

_counter = itertools.count(1)  # next() gives a fresh number -> unique values

PASSWORD = 'S3cure-Passw0rd!'  # throw-away value used only inside tests

# Smallest valid GIF. ImageField validates uploads with Pillow, so a fake
# text file named "x.gif" would be rejected.
_TINY_GIF = (
    b'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!\xf9\x04'
    b'\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'
)


def make_image(name='photo.gif'):
    return SimpleUploadedFile(name, _TINY_GIF, content_type='image/gif')


def make_user(username=None, with_profile=True, age=25):
    """An AppUser plus (like the register view does) its Profile."""
    username = username or f'user{next(_counter)}'
    user = get_user_model().objects.create_user(
        username=username, email=f'{username}@example.com', password=PASSWORD,
    )
    if with_profile:
        Profile.objects.create(user=user, first_name='Test', last_name='User', age=age)
    return user


def make_pet(profile, **overrides):
    data = {'name': 'Rex', 'species': 'dog', 'age': 3, 'weight': 12.5, 'owner': profile}
    data.update(overrides)
    return Pet.objects.create(**data)


def make_hotel(city='Sofia', **overrides):
    n = next(_counter)
    data = {
        'name': f'Pet Oasis {city}', 'city': city, 'street': 'Main', 'street_number': n,
        'phone': '0888123456', 'email': f'hotel{n}@example.com', 'description': 'A cosy place.',
    }
    data.update(overrides)
    return PetHotel.objects.create(**data)
