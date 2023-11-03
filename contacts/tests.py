from django.test import TestCase

from contacts.models import Contact


# Create your tests here.
class TestContact(TestCase):
    def test_contact(self):
        c = Contact.objects.create(
            name='test')

        print(c.created_at)
        print(c.last_updated)

        c = Contact.objects.first()
        print(c.created_at)
        print(c.last_updated)
