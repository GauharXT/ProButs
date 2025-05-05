from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password', 'password2']
        extra_kwargs = {
            'email': {'required': True},
            'username': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})

        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "Email уже зарегистрирован"})

        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
