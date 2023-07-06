from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'userName',  'firstName', 'lastName', 'email', 'phoneNumber', 'hashed_otp']
        extra_kwargs = {'password': {'write_only': True}}