from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from captcha.fields import ReCaptchaField


class RegistrationForm(UserCreationForm):
    ''' registration form class imported from UserCreationForm '''
    email = forms.EmailField(required=True)
    captcha = ReCaptchaField(label='')

    class Meta:
        ''' visible fields when registering '''
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'captcha'
        )

    def save(self, commit=True):
        ''' save to database when cleaned '''
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    ''' editing profile via UserChangeForm '''

    class Meta:
        ''' visible fields when editing profile '''
        model = User
        fields = (
            'email',
            'first_name',
            'last_name'
        )
