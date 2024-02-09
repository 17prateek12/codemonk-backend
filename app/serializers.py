from rest_framework import serializers
from .models import Paragraph
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    
    class Meta:
        model=User
        fields=['id','name', 'email', 'username', 'dob', 'createdAt', 'modifiedAt', 'isAdmin']
        
    def get_isAdmin(self, obj):
        return obj.is_staff
        
    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.username
        return name
       
        
class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields=['id','name', 'email', 'username', 'dob', 'createdAt', 'modifiedAt', 'token', 'isAdmin']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
        



class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ('id', 'content')

