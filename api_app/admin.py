from django.contrib import admin
from .models import Publication, Category, User, Books, Author
# Register your models here.

admin.site.register(Publication)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Books)
admin.site.register(Author)

