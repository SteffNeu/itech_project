from django import forms
from antifu.models import UserProfile, Comment
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

class ContactForm(forms.Form):
    #name = form.CharField(required=True)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea, required=True, max_length=1000)
    class Meta:
        model = Comment
        fields = ('comment',)