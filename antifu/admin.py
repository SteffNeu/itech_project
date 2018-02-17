from django.contrib import admin
from antifu.models import Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields =  {'slug':('name',)}

# Register your models here.
admin.site.register(Category, CategoryAdmin)
