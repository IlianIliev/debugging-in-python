from time import mktime

from django.db import models
from utils.models import DateTimeField


# Create your models here.
class Contact(models.Model):
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField(blank=True)
    created_at = DateTimeField(auto_now_add=True)
    last_updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_hash(self):
        last_updated_timestamp = int(mktime(self.last_updated.timetuple()))
        return f'{self.pk}_{last_updated_timestamp}'
