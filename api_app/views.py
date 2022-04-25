from rest_framework.response import Response
from rest_framework.decorators import api_view
from api_app.models import Books, User
from .serializers import BookSerializer, UserSerializer

@api_view(['GET'])
def getBooks(request):
    book = Books.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)
# Create your views here.
