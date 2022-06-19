from rest_framework import serializers
from rest_framework import status
from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = HobbyModel
        fields = ["name"]

class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True)
    class Meta:
        model = UserProfileModel
        fields = ["introduction", "birthday", "age", "hobby"]


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()

    class Meta:
        model=UserModel
        fields = ["username", "fullname", "join_date", "userprofile"]


