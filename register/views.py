from rest_framework import generics 
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny 
from .models import CustomUser


class RegisterView(generics.CreateAPIView): 
    queryset = CustomUser.objects.all() 
    permission_classes = (AllowAny,) 
    serializer_class = RegisterSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

