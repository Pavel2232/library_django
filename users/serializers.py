from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from users.tasks import send_welcome_email_task
from users.models import User


class SignupUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, validators=[validate_password], write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name']

    def create(self, validated_data) -> User:
        user = User.objects.create_user(**validated_data)
        send_welcome_email_task.delay(
            user.email, user.first_name
        )

        return user


class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name']
        read_only_fields = ['id', 'email', 'first_name']


class EditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name']
        read_only_fields = ['id']


class UpdatePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(max_length=100, validators=[validate_password])
    old_password = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'new_password', 'old_password', 'first_name']
        read_only_fields = ['id', 'email', 'first_name']

    def update(self, instance, validated_data):
        validated_data['new_password'] = make_password(validated_data['new_password'])
        return super().update(instance, validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'email')
