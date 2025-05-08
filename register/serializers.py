from rest_framework import serializers
<<<<<<< HEAD
from .models import User
from django.contrib.auth.password_validation import validate_password

=======
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

>>>>>>> origin/dan
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
<<<<<<< HEAD
            'username': {'required': True},
=======
            'username': {'required': True}
>>>>>>> origin/dan
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
<<<<<<< HEAD
            raise serializers.ValidationError({"password": "Пароли не совпадают"})

        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "Email уже зарегистрирован"})
=======
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "Email already exists"})

        if 'phone' in attrs and User.objects.filter(phone=attrs['phone']).exists():
            raise serializers.ValidationError({"phone": "Phone already exists"})
>>>>>>> origin/dan

        return attrs

    def create(self, validated_data):
<<<<<<< HEAD
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
=======
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone=validated_data.get('phone', None)
        )
        return user
>>>>>>> origin/dan
