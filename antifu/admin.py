from django.contrib import admin
from antifu.models import Category,Comment,Post,User


# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post)