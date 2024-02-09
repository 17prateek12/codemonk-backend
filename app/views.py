from rest_framework import generics
from .models import Paragraph
from .serializers import ParagraphSerializer, UserSerializer, UserSerializerWithToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password

User=get_user_model()

# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs): 
        data = super().validate(attrs)
        serializer= UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k]=v
        return data 
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
@api_view(['GET'])
def getuser(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def registeruser(request):
    data= request.data
    try:
        user = User.objects.create(
            first_name=data['name'],
            email=data['email'],
            username=data['username'],
            dob=data['dob'],
            password=make_password(data['password']),
        )
        serializer= UserSerializerWithToken(user,many=False)
        return Response(serializer.data)
    except:
        message={'User with username already exist'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)


class ParagraphList(generics.ListCreateAPIView):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer

class WordSearch(generics.ListAPIView):
    serializer_class = ParagraphSerializer

    def get_queryset(self):
        word = self.kwargs['word'].lower()
        return Paragraph.objects.filter(content__icontains=word)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
