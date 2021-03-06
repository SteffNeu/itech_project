from django import forms
from antifu.models import UserProfile, Comment, ContactUsEmail, Category, Post
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

class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=50)
    from_email = forms.EmailField(required=True, label='Email')
    subject = forms.CharField(required=True, max_length=50, label='Subject')
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=1024)

    class Meta:
        model = ContactUsEmail
        fields = ('name', 'from_email', 'subject', 'message',)


class uploadPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    title = forms.CharField(max_length=64)
    context = forms.CharField(max_length=512)
    tags = forms.CharField(max_length=128)
    picturePost = forms.ImageField(required=True)

    class Meta:
        model = Post
        fields = ('category', 'title', 'context', 'tags', 'picturePost',)
