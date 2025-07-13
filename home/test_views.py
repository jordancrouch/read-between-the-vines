from django.test import TestCase
from django.urls import reverse


class TestHomepageView(TestCase):
    """
    Tests for the homepage view
    """

    def test_render_homepage(self):
        """
        Test for rendering the homepage
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

    def test_homepage_context_contains_expected_data(self):
        """
        Test the homepage contains the expected data
        """
        response = self.client.get(reverse("home"))
        context = response.context
        self.assertIn("currently_reading_books", context)
        self.assertIn("to_be_read_books", context)
        self.assertIn("contact_url", context)
