from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .tokens import get_tokens_for_user
from .models import MyModel
from rest_framework import status, generics
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import MyModelSerializer, LoginSerializer
from django.contrib.auth.hashers import check_password

class UserRegisterAPIView(generics.CreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({
                'details': serializer.data,
                'token': token
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserLoginAPIView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"msg": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = MyModel.objects.get(email=email)
            if check_password(password, user.password):
                token = get_tokens_for_user(user)
                return Response({
                    'token': token,
                    'msg': 'Login successful'
                }, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
        except MyModel.DoesNotExist:
            return Response({"detail": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
