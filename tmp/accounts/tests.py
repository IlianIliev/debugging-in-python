from django.test import TestCase
from accounts.models import User


class Test(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )

        print(user.settings)
