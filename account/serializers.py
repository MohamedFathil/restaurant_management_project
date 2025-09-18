from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
    
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['user', 'phone_number']

    def update(self, instance, validated_data):
        # extract nested user data
        user_data = validated_data.pop('user',[])

        # update
        user = instance.user
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance