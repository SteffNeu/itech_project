from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique = True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    totallove = models.IntegerField(default = 0)

    def __str__(self):
        return self.user.username



class Post(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    date = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=64)
    context = models.TextField(max_length=512)
    tags = models.CharField(max_length=128)
    grammarFail = models.IntegerField(default=0)
    logicFail = models.IntegerField(default=0)
    toxicity = models.IntegerField(default=0)
    harmful = models.IntegerField(default=0)
    report = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    picturePost = models.ImageField(upload_to='post_pictures')

    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, null=True)
    user = models.ForeignKey(UserProfile, null=True)
    date = models.DateField(default=datetime.date.today)
    comment = models.TextField(max_length=1024)
    loveliness = models.IntegerField(default=0)
    burnfactor = models.IntegerField(default=0)
    logicRating = models.IntegerField(default=0)
    accuracyRating = models.IntegerField(default=0)

    def __str__(self):
        return self.comment

class FAQ(models.Model):
    questions = models.TextField(blank=True)
    answers = models.TextField(blank=True)

    def __str__(self):
        return self.questions

class PersonalHelp(models.Model):
    cbTitle = models.TextField(blank=True)
    cbHref = models.TextField(blank=True)

    preventionTitle = models.TextField(blank=True)
    preventionHref = models.TextField(blank=True)

    interventionTitle = models.TextField(blank=True)
    interventionHref = models.TextField(blank=True)

    helpTitle = models.TextField(blank=True)
    helpHref = models.TextField(blank=True)

    suiPrevTitle = models.TextField(blank=True)
    suiPrevHref = models.TextField(blank=True)

    #def __str__(self):
    #    return self.title

class ContactUsEmail(models.Model):
    name = models.CharField(default=0, max_length=50)
    from_email = models.EmailField(default=0)
    subject = models.CharField(default=0, max_length=50)
    message = models.CharField(default=0, max_length=1024)

    def save(self, *args, **kwargs):
        super(ContactUsEmail, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
