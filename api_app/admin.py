from django.contrib import admin
from .models import  SubCategory, Category, Books, NewUser, Email, NewUser
# Register your models here.


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(NewUser)
admin.site.register(Books)
admin.site.register(Email)
