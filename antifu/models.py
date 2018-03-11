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


# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=128, unique=True)
#
#     def save(self, *args, **kwargs):
#         super(Category, self).save(*args, **kwargs)
#
#     class Meta:
#         verbose_name_plural = 'Categories'
#
#     def __str__(self):
#         return self.name



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
    title = models.TextField(blank=True)
    href = models.TextField(blank=True)

    def __str__(self):
        return self.title
