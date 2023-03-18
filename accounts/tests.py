from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = "3k3n3", email = "3k3n3@test.com", password = "testpwd123"
        )
        self.assertEqual(user.username, "3k3n3")
        self.assertEqual(user.email, "3k3n3@test.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username = "3k3n3_admin", email = "3k3n3_admin@test.com", password = "testpwd123"
        )
        self.assertEqual(user.username, "3k3n3_admin")
        self.assertEqual(user.email, "3k3n3_admin@test.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)