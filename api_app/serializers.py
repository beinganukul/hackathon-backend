from rest_framework import serializers
from api_app.models import Books, NewUser, Email

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['id', 'first_name', 'last_name']

#class AuthorSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Author
#        fields = '__all__' 

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__' 

class BookSerializer(serializers.ModelSerializer):
    #user = UserSerializer(many=True)
    class Meta:
        model = Books
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['id', 'user_name', 'first_name', 'last_name', 'phone', 'email', 'credit','invites', 'note'] 

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = NewUser
        fields = ['email', 'user_name', 'password', 'password2', 'first_name', 'last_name']
        extra_kwargs = {
                'password': {'write_only': True}
                }
    def save(self):
        user = NewUser(email=self.validated_data['email'], first_name = self.validated_data['first_name'],last_name = self.validated_data['last_name'], user_name = self.validated_data['user_name'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user
