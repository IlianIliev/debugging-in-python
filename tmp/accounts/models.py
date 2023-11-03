from django.contrib.auth.models import AbstractUser

from django.db import models
from django.db.models.fields.json import JSONField


class User(AbstractUser):
    DEFAULT_SETTINGS = {
        "language": "en",
        "theme": "dark",
        "notifications": True,
    }

    settings = JSONField(default=DEFAULT_SETTINGS)


