from django.contrib import admin
from .models import Books, NewUser, Email, NewUser

#SubCategory, Category, # Register your models here.


#admin.site.register(Category)
#admin.site.register(SubCategory)
admin.site.register(NewUser)
admin.site.register(Books)
admin.site.register(Email)
