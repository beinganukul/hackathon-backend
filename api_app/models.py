from django.db import models 
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

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

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')
        return self.create_user(email, user_name, first_name, last_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, last_name, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, user_name = user_name, first_name = first_name, last_name = last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

class NewUser(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone = models.IntegerField(null=True)
    #(validators=[MaxValueValidator(999999999)])
    email = models.EmailField(unique=True)
    credit = models.IntegerField(null=True)
    #(validators=[MaxValueValidator(999)])
    note = models.CharField(max_length = 300)
    objects = CustomAccountManager()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.user_name

class Email(models.Model):
    email = models.EmailField()
    is_registered = models.BooleanField(default=False)
    def __str__(self):
        return self.email

class Books(models.Model):
    user = models.ManyToManyField(NewUser)
    bname = models.CharField(max_length = 300)
    author = models.ManyToManyField(Author)
    revision = models.CharField(max_length = 4)
    publication = models.ForeignKey(Publication, on_delete=models.DO_NOTHING)
    category = models.ManyToManyField(Category)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.bname

