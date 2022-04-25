from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from api_app.models import Books, NewUser
from .serializers import BookSerializer, UserSerializer, ProfileSerializer, RegistrationSerializer# PasswordChangeSerializer
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['GET'])
def getBooks(request):
    book = Books.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUser(request):
    user = NewUser.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request, pk):
    profile = NewUser.objects.get(id = pk)
    serializer = ProfileSerializer(profile, many = False)
    return Response(serializer.data)

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
