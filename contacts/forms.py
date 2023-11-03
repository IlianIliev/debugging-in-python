from django import forms

from contacts.models import Contact
from contacts.utils import get_latest_hash


class ContactForm(forms.ModelForm):    # hash = forms.CharField(required=True)
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean(self):
        cleaned_data = super().clean()
        user_hash = self.request.session.get('latest_hash')
        latest_hash = get_latest_hash(self.request.user)
        if user_hash != latest_hash:
            raise forms.ValidationError('Someone else has modified the data. Please Re-Sync and try again.')

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.owner = self.request.user

        if commit:
            instance.save()

        return instance

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'message')
