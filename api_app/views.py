from rest_framework.response import Response
from rest_framework.decorators import api_view
from api_app.models import Books, NewUser
from .serializers import BookSerializer, UserSerializer, ProfileSerializer, RegistrationSerializer# PasswordChangeSerializer
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
#from .utils import get_tokens_for_user

@api_view(['GET'])
def getBooks(request):
    book = Books.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request):
    user = NewUser.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProfile(request, pk):
    profile = NewUser.objects.get(id = pk)
    serializer = ProfileSerializer(profile, many = False)
    return Response(serializer.data)

#@api_view(['POST'])
#def registeruser(request):
#    serializer = RegistrationSerializer(data=request.data)
#    if serializer.is_valid():
#        serializer.save()
#        return Response(serializer.data, status=status.HTTP_201_CREATED)
#    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
