from django.contrib import admin
from .models import  Category, Books, NewUser, Email, NewUser
# Register your models here.


admin.site.register(Category)
admin.site.register(NewUser)
admin.site.register(Books)

# @admin.register(Books)
# class AuthorAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug':('bname',),}

admin.site.register(Email)
