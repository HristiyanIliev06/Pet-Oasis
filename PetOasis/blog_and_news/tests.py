import shutil
import tempfile

from django.test import TestCase, override_settings
from django.urls import reverse

from blog_and_news.models import PawPost
from core.factories import make_image, make_user

TEMP_MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class PawPostTests(TestCase):

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def test_str_is_title_and_timestamp_is_automatic(self):
        post = PawPost.objects.create(title='Nap time', description='Zzz', image=make_image())
        self.assertEqual(str(post), 'Nap time')
        self.assertIsNotNone(post.when_uploaded)  # auto_now_add
        self.assertTrue(post.image.name.startswith('profile_pics/pawposts/'))


class BlogPageTests(TestCase):

    def test_page_loads_for_anonymous_and_logged_in_visitors(self):
        url = reverse('blog_and_news')
        self.assertEqual(self.client.get(url).status_code, 200)

        self.client.force_login(make_user())
        self.assertEqual(self.client.get(url).status_code, 200)
