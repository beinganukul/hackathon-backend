from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from api_app.models import Books, NewUser, Email
from .serializers import BookSerializer, UserSerializer, ProfileSerializer, RegistrationSerializer, EmailSerializer# PasswordChangeSerializer
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import json
import io
from rest_framework.parsers import JSONParser

@api_view(['GET'])
def getBooks(request):
    book = Books.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def getEmail(request):
    email = Email.objects.filter(email=request.data["email"])
    serializer = EmailSerializer(email, many=True)
    try:
        status = Email.objects.get(email__exact=request.data["email"])
        return Response(serializer.data)
    except:
        return Response({ "response":"email doesn't exist in invite table"})
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUsers(request):
    user = NewUser.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getInvite(request):
    invites = NewUser.objects.get(id=request.user.id)
    emailserializer = EmailSerializer(data=request.data)
    if invites.invites < 2:
        if emailserializer.is_valid():
            invites.invites = invites.invites + 1
            invites.save(update_fields=['invites'])
            emailserializer.save()
            return Response(emailserializer.data)
        else:
            return Response({"response":"email already exists or json is incorrect"})
    else:
        return Response({"response":"invites reached limit"})
    return Response(emailserializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    profile = NewUser.objects.get(id =request.user.id)
    serializer = ProfileSerializer(profile, many = False)
    return Response(serializer.data)

class RegistrationView(APIView):
    def post(self, request):
        email = Email.objects.filter(email=request.data["email"])
        emailserializer = EmailSerializer(email, many=True)
        try:
            status = Email.objects.get(email__exact=request.data["email"])
        except:
            return Response({"response":"sorry your email address doesn't exist in invite list"})
        if status.is_registered == True:
            return Response({"response":"user with this email already exists"})
        else:
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                tochange = Email.objects.get(email__exact=request.data["email"])
                tochange.is_registered = True
                tochange.save(update_fields=['is_registered'])
                return Response(serializer.data)# , status=status.HTTP_201_CREATED)
        return Response(serializer.errors)#, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def userlogout(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        #return Response(status=status.HTTP_205_RESET_CONTENT)
        return Response({'msg': 'Logged Out'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def putBook(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
