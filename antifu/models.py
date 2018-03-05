from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


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


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.TextField(max_length=1024)
    loveliness = models.IntegerField(default=0)
    burnfactor = models.IntegerField(default=0)
    logicRating = models.IntegerField(default=0)
    accuracyRating = models.IntegerField(default=0)

    def __str__(self):
        return self.comment


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE,null=True)
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


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    comments = models.ForeignKey(Comment, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
