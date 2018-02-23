from django import forms
from antifu.models import UserProfile
from django.contrib.auth.models import User
from registration.forms import RegistrationForm


class UserForm(RegistrationForm):

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args,**kwargs)

        for key in self.fields:
            self.fields[key].required = True


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)