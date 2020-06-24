from rest_framework import serializers
from lokalhood_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes fields for UserProfile Model"""
    class Meta :
        model = models.UserProfile
        fields = ("id","phone_no","name","email","password")
        extra_kwargs = {
            'password' :{
                'write_only' : True,
                'style' : {'input_type' : 'password'}
            }
        }
    def create(self, validated_data):
        """ Create and return user"""
        user = models.UserProfile.objects.create_user(
            phone_no = validated_data['phone_no'],
            name = validated_data['name'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            instance.set_password(password)
            password = validated_data.pop('password')

        return super().update(instance, validated_data)

class ShopSerializer(serializers.ModelSerializer):
    """Serializes fields for Shop Model"""
    class Meta :
        model = models.Shop
        fields = ("id","name","locality","category")


class RequestSerializer(serializers.ModelSerializer):
    """Serializes fields for Request Model"""
    class Meta :
        model = models.Request
        fields = ("id","user","shop","items","deliver_addr","details","status", "created_on")
        extra_kwargs = {'user': {'read_only': True}}
