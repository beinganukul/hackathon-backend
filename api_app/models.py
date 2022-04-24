from django.db import models 
from django.core.validators import MaxValueValidator

class Category(models.Model):
    category = models.CharField(max_length = 50)
    def __str__(self):
        return self.category

class Publication(models.Model):
    pname = models.CharField(max_length = 300)
    def __str__(self):
        return self.pname

class Author(models.Model):
    author_first_name = models.CharField(max_length = 50)
    author_last_name = models.CharField(max_length = 50)
    def __str__(self):
        return self.author_first_name + ' ' + self.author_last_name

class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone = models.IntegerField(validators=[MaxValueValidator(999999999)])
    email_address = models.EmailField()
    credit = models.IntegerField(validators=[MaxValueValidator(999)])
    note = models.TextField(blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Books(models.Model):
    user = models.ManyToManyField(User)
    bname = models.CharField(max_length = 300)
    author = models.ManyToManyField(Author)
    revision = models.CharField(max_length = 4)
    publication = models.ForeignKey(Publication, on_delete=models.DO_NOTHING)
    category = models.ManyToManyField(Category)
    description = models.CharField(max_length = 500)
    def __str__(self):
        return self.bname

