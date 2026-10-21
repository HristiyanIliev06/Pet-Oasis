from django.test import TestCase
from django.urls import reverse


class AboutUsPageTests(TestCase):
    url = reverse('about_us')

    def test_anonymous_visitor_sees_the_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us.html')
        self.assertIsNone(response.context['profile'])
