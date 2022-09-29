from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")

    def validate(self, attrs):
        email = attrs.get("email")
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": ("Email is already in use")})
        return super().validate(attrs)

    def created(self, validated_data):
        return User.objects.create_user(**validated_data)
