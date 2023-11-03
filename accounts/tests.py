from django.test import TestCase
from accounts.models import User, DEFAULT_SETTINGS


class Test(TestCase):
    def test_create_user(self):
        admin = User.objects.create_user(
            username='admin',
            password='testpass123',
        )

        self.assertEqual(admin.settings, DEFAULT_SETTINGS)

        user = User.objects.create_user(
            username='John Doe',
            password='testpass123',
            settings={"theme": "light"},
        )

        expected_settings = DEFAULT_SETTINGS
        expected_settings.update({"theme": "light"})
        self.assertEqual(user.settings, expected_settings)

        user2 = User.objects.create_user(
            username='Jane Doe',
            password='testpass123',
        )

        assert user2.settings == DEFAULT_SETTINGS

