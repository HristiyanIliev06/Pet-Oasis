import shutil
import tempfile

from django.core.exceptions import ValidationError
from django.test import TestCase, override_settings
from django.urls import reverse

from core.factories import make_image, make_pet, make_user
from pets.forms import RegisterPetForm
from pets.models import Pet

# Uploads go to a throw-away folder, never to the real media/ directory
TEMP_MEDIA_ROOT = tempfile.mkdtemp()


class PetModelTests(TestCase):

    def test_str_is_the_name(self):
        self.assertEqual(str(make_pet(make_user().profile, name='Buddy')), 'Buddy')

    def test_negative_weight_is_invalid_but_zero_is_allowed(self):
        owner = make_user().profile
        with self.assertRaises(ValidationError) as ctx:
            Pet(name='Ghost', species='cat', age=1, weight=-1, owner=owner).full_clean()
        self.assertIn('weight', ctx.exception.message_dict)
        Pet(name='Feather', species='bird', age=1, weight=0, owner=owner).full_clean()  # boundary

    def test_form_rejects_unknown_species_and_hides_owner(self):
        form = RegisterPetForm(data={'name': 'Smaug', 'species': 'dragon', 'age': 1, 'weight': 1})
        self.assertFalse(form.is_valid())
        self.assertIn('species', form.errors)
        # the owner comes from the logged-in user, never from the submitted form
        self.assertNotIn('owner', form.fields)


# override_settings as a class decorator applies the temporary value to every test
@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class PetViewTests(TestCase):

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def setUp(self):
        self.user = make_user('creator')
        self.client.force_login(self.user)

    def test_add_pet_form_creates_pet_owned_by_current_user(self):
        response = self.client.post(reverse('add_pet'), {
            'name': 'Rex', 'species': 'dog', 'breed': 'Husky', 'age': 4, 'weight': 20.5,
            'image': make_image('rex.gif'),  # a file in the data makes it a multipart upload
        })

        self.assertRedirects(response, reverse('show_profile'))
        pet = Pet.objects.get()  # .get() also proves there is exactly one pet
        self.assertEqual(pet.owner, self.user.profile)
        self.assertTrue(pet.image.name.startswith('profile_pics/pets/'))

    def test_owner_can_delete_own_pet(self):
        pet = make_pet(self.user.profile)
        response = self.client.post(reverse('delete_pet', kwargs={'pk': pet.pk}))
        self.assertRedirects(response, reverse('show_profile'))
        self.assertFalse(Pet.objects.exists())
