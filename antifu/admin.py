from django.contrib import admin
from antifu.models import Category, Post, Comment, UserProfile

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(UserProfile)
