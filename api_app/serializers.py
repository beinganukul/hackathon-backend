from rest_framework import serializers
from api_app.models import Books, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']

class BookSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    class Meta:
        model = Books
        fields = '__all__'


