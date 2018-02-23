from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique = True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

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
    comment = models.TextField(max_length=1024)
    loveliness = models.IntegerField()
    burnfactor = models.IntegerField()
    logicRating = models.IntegerField()
    accuracyRating = models.IntegerField()

    def __str__(self):
        return self.comment


class Post(models.Model):
    category = models.ManyToManyField(Category)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    context = models.TextField(max_length=512)
    tags = models.CharField(max_length=128)
    grammarFail = models.IntegerField()
    logicFail = models.IntegerField()
    toxicity = models.IntegerField()
    harmful = models.IntegerField()
    report = models.IntegerField()
    views = models.IntegerField()
    picturePost = models.ImageField()

    def __str__(self):
        return self.picturePost


class User(models.Model):
    comments = models.ForeignKey(Comment)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    email = models.EmailField(max_length=128, unique=True)
    username = models.CharField(max_length=128, unique=True)
    #profileRef = models.ImageField()

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username




