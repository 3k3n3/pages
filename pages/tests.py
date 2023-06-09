from django.test import SimpleTestCase
from django.urls import resolve, reverse
from .views import HomePageView
# Create your tests here.


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exist_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "home page")

    def test_homepage_does_not_contain_correct_html(self):
        self.assertNotContains(self.response, "some text...")

    def test_homepage_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)