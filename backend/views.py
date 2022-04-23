from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt 
import json

