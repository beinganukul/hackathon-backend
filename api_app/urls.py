from django.urls import path
from . import views

urlpatterns = [
        path('books', views.getBooks),
        path('users', views.getUser),
        ]
