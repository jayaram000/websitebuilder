from rest_framework import serializers
from .models import User,Website
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['email','password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Credentials or mail not found")


class WebsiteSerializer(serializers.ModelSerializer):
    preview_url = serializers.SerializerMethodField()

    class Meta:
        model = Website
        fields = '__all__'

    def get_preview_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(f'/api/preview/{obj.preview_id}/')
        return f'/api/preview/{obj.preview_id}/'
