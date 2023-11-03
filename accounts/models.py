from django.contrib.auth.models import AbstractUser

from django.db.models.fields.json import JSONField


DEFAULT_SETTINGS = {
    "language": "en",
    "profile_header": "",
    "subscribe_to_newsletter": False,
}


class User(AbstractUser):
    settings = JSONField(default=DEFAULT_SETTINGS)

    def save(self, **kwargs):
        if not self.pk:
            # For new users we want to set the default settings
            user_settings = DEFAULT_SETTINGS
            user_settings.update(self.settings)
            self.settings = user_settings

        super().save(**kwargs)
