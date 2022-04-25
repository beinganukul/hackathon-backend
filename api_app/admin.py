from django.contrib import admin
from .models import Publication, Category, Books, Author, NewUser #User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django import forms
from .models import NewUser
# Register your models here.


admin.site.register(Publication)
admin.site.register(Category)
#admin.site.register(User)
admin.site.register(NewUser)
admin.site.register(Books)
admin.site.register(Author)

