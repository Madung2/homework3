from rest_framework import serializers
from rest_framework import status
from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel
from blog.models import Article as ArticleModel
from blog.models import Comment as CommentModel

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ["content"]

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ["title", "contents"]

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
    article = ArticleSerializer(many=True, source = "article_set")#역참조
    comment = CommentSerializer(many=True, source = "comment_set")


    class Meta:
        model=UserModel
        fields = ["username", "fullname", "join_date", "userprofile", "article","comment"]



