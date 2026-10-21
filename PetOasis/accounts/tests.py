from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from accounts.models import Profile
from core.factories import PASSWORD, make_pet, make_user
from pets.models import Pet

User = get_user_model()


class AppUserAndProfileModelTests(TestCase):

    def test_create_user_hashes_password_and_is_not_staff(self):
        user = User.objects.create_user('alice', 'alice@example.com', 'pw12345678')
        self.assertTrue(user.check_password('pw12345678'))
        self.assertNotEqual(user.password, 'pw12345678')  # never stored in clear text
        self.assertFalse(user.is_staff or user.is_superuser)

    def test_profile_under_18_fails_validation_but_18_passes(self):
        user = make_user(with_profile=False)
        # full_clean() runs field validators (save() alone does not)
        with self.assertRaises(ValidationError) as ctx:
            Profile(user=user, first_name='A', last_name='B', age=17).full_clean()
        self.assertIn('age', ctx.exception.message_dict)
        Profile(user=user, first_name='A', last_name='B', age=18).full_clean()  # boundary: no error


class RegisterViewTests(TestCase):
    url = reverse('register')
    valid = {
        'username': 'newbie', 'email': 'newbie@example.com', 'first_name': 'New',
        'last_name': 'Bie', 'age': 30, 'password1': PASSWORD, 'password2': PASSWORD,
    }

    def test_valid_submission_creates_user_and_one_profile_and_logs_in(self):
        response = self.client.post(self.url, self.valid)

        self.assertRedirects(response, reverse('index'))
        user = User.objects.get(username='newbie')
        self.assertEqual(Profile.objects.filter(user=user).count(), 1)
        self.assertEqual(user.profile.age, 30)
        self.assertEqual(int(self.client.session['_auth_user_id']), user.pk)  # logged in

    def test_underage_submission_creates_nothing(self):
        response = self.client.post(self.url, {**self.valid, 'age': 12})
        self.assertEqual(response.status_code, 200)  # form shown again with errors
        self.assertFalse(User.objects.exists())
        self.assertFalse(Profile.objects.exists())


class LoginTests(TestCase):

    def test_valid_credentials_redirect_home(self):
        make_user('dave')
        response = self.client.post(reverse('login'), {'username': 'dave', 'password': PASSWORD})
        self.assertRedirects(response, reverse('index'))



class LoginRequiredTests(TestCase):

    def test_protected_pages_redirect_anonymous_visitors(self):
        # pets' add/delete pages use the same LoginRequiredMixin
        protected = [
            reverse('edit_profile'),
            reverse('delete_account'),
            reverse('add_pet'),
            reverse('delete_pet', kwargs={'pk': 1}),
        ]
        for url in protected:
            with self.subTest(url=url):  # report each URL separately
                response = self.client.get(url)
                self.assertEqual(response.status_code, 302)
                self.assertIn('next=', response.url)  # remembers where to return after login


class ProfileAccountViewTests(TestCase):

    def setUp(self):
        self.user = make_user('owner')
        self.client.force_login(self.user)  # skip the login form

    def test_profile_page_lists_only_my_pets(self):
        make_pet(self.user.profile, name='Mine')
        make_pet(make_user('other').profile, name='NotMine')

        response = self.client.get(reverse('show_profile'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual([p.name for p in response.context['pets']], ['Mine'])

    def test_edit_account_updates_username_and_email(self):
        response = self.client.post(reverse('edit_profile'), {
            'username': 'renamed', 'email': 'renamed@example.com', 'old_password': PASSWORD,
        })

        self.assertRedirects(response, reverse('show_profile'))
        self.user.refresh_from_db()  # reload from the database
        self.assertEqual((self.user.username, self.user.email), ('renamed', 'renamed@example.com'))

    def test_edit_account_with_wrong_old_password_changes_nothing(self):
        response = self.client.post(reverse('edit_profile'), {
            'username': 'renamed', 'email': 'renamed@example.com', 'old_password': 'wrong',
        })
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'owner')

    def test_delete_account_removes_user_profile_and_pets(self):
        make_pet(self.user.profile)
        response = self.client.post(reverse('delete_account'), {
            'username': 'owner', 'password': PASSWORD, 'confirm_password': PASSWORD,
        })

        self.assertRedirects(response, reverse('index'))
        self.assertFalse(User.objects.filter(username='owner').exists())
        self.assertFalse(Profile.objects.exists())  # CASCADE from the user
        self.assertFalse(Pet.objects.exists())      # CASCADE from the profile
