from django import forms
from antifu.models import UserProfile
from django.contrib.auth.models import User
from registration.forms import RegistrationForm


class UserForm(RegistrationForm):
    first_name = forms.CharField(max_length=30,required=True)
    last_name = forms.CharField(max_length=150,required=True)
    username = forms.CharField(max_length=191,required=True)
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email')


        #self.userprofileform = UserProfileForm(*args,**kwargs.copy())
        #self.fields.update(self.userprofileform.fields)
        #self.initial.update(self.userprofileform.initial)



class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    class Meta:
        model = UserProfile
        fields = ('picture',)
