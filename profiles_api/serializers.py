import re
from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'password', 'name', 'phone_number', 'dob', 'gender', 'address')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            phone_number=validated_data['phone_number'],
            dob=validated_data["dob"],
            gender=validated_data["gender"],
            address=validated_data["address"],
            password=validated_data['password'],

        )

        return user

    def validate_phone_number(self, value):
        Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
        if not Pattern.match(value):
            raise serializers.ValidationError("Phone number is invalid")
        return value