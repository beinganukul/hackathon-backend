from django.db import models

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
    phone = models.IntegerField(max_length = 10)
    email_address = models.EmailField()
    credit = models.IntegerField(max_length = 3)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
# Create your models here.
class Books(models.Model):
    user = models.ManyToManyField(User)
    bname = models.CharField(max_length = 300)
    author = models.ManyToManyField(Author)
    revision = models.CharField(max_length = 4)
    publication = models.ForeignKey(Publication, on_delete=models.DO_NOTHING)
    category = models.ManyToManyField(Category)
    def __str__(self):
        return self.bname

