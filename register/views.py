from rest_framework import generics 
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

class RegisterView(generics.CreateAPIView): 
    queryset = CustomUser.objects.all() 
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


    def perform_create(self, serializer): 
        if self.request.user.is_authenticated:
            if self.request.user.role == CustomUser.TUTOR:
                raise PermissionDenied("Tutors cannot create users.")
            elif self.request.user.is_staff:
                role = self.request.data.get('role')
                if role == CustomUser.TUTOR:
                    user = serializer.save(role=CustomUser.TUTOR, is_staff=True)
                elif role == CustomUser.STUDENT: 
                    user = serializer.save(role=CustomUser.STUDENT)
                else: 
                    raise serializers.ValidationError("Invalid role specified.")
            else:
                raise PermissionDenied("You do not have permission to create users.")
        else:
            user = serializer.save(role=CustomUser.STUDENT)
        return Response({ 
            'message': 'User registered successfully', 
            'username': user.username, 
            'email': user.email, 
            'role': user.role, 
            'first_name': user.first_name, 
            'last_name': user.last_name, 
            'dob': user.dob, 
            'mobile': user.mobile })


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CheckSessionView(APIView):
    def get(self, request, *args, **kwargs):
        session_data = {
            'refresh_token': request.session.get('refresh_token'),
            'access_token': request.session.get('access_token'),
            'user_email': request.session.get('user_email'),
        }
        return Response(session_data)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = request.user
        print(user.role)
        if user.role == CustomUser.TUTOR or user.role == CustomUser.STUDENT:
            user_data = {
                "name": user.get_full_name(),
                "email": user.email,
                "mobile": user.mobile,
            }
            return Response(user_data)
        else:
            return Response({"message": "you dont have access"})

class StudentDetailView(generics.CreateAPIView):
    queryset = StudentDetails.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = StudentProfileSerializer

    def get_object(self):
        user = self.request.user
        if user.role == 'student':
            return user.student_profile
        else:
            return PermissionDenied("You do not have permission to view this profile.")

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        request.session.flush()
        return Response({"message": "logged out"})