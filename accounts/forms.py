from django import forms

from accounts.models import User


class UserForm(forms.ModelForm):
    profile_header = forms.CharField(max_length=255, required=False)
    subscribe_to_newsletter = forms.ChoiceField(choices=(
        ('', 'No'),
        ('True', 'Yes'),
    ), required=False, label='Subscribe to newsletter?')

    class Meta:
        fields = ('username', 'password')
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['profile_header']:
            user.settings['profile_header'] = self.cleaned_data['profile_header']

        if self.cleaned_data['subscribe_to_newsletter'] == 'True':
            user.settings['subscribe_to_newsletter'] = True

        if commit:
            user.set_password(self.cleaned_data['password'])
            user.save()

        return user
