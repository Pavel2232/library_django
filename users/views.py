from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from users.serializers import SignupUserSerializer, LoginUserSerializer


class SignupView(CreateAPIView):
    serializer_class = SignupUserSerializer


class LoginUserView(CreateAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(self.serializer_class(user).data, status=status.HTTP_201_CREATED)
        else:
            raise ValidationError({'email or password': "Неверный"})
