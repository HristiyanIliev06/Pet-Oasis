import shutil
import tempfile

from django.test import TestCase, override_settings
from django.urls import reverse

from blog_and_news.models import PawPost
from core.factories import make_hotel, make_image

TEMP_MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class HomePageTests(TestCase):
    url = reverse('index')

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def test_empty_site_still_renders_for_anonymous_visitor(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context['profile'])

    def test_home_page_caps_hotels_at_three_and_pawposts_at_seven(self):
        for city in ('Sofia', 'Varna', 'Ruse', 'Plovdiv', 'Burgas'):
            make_hotel(city)
        # bulk_create inserts all nine rows with a single query
        PawPost.objects.bulk_create(
            [PawPost(title=f'Post {i}', description='d', image=make_image(f'{i}.gif')) for i in range(9)]
        )

        context = self.client.get(self.url).context

        self.assertEqual(len(context['top_3_facilities']), 3)
        self.assertEqual(len(context['pawposts']), 7)
