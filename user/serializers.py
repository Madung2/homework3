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
    userprofile = UserProfileSerializer(read_only=True)
    article = ArticleSerializer(
        many=True, source="article_set", read_only=True)  # 역참조
    comment = CommentSerializer(
        many=True, source="comment_set", read_only=True)  # 역참조

    # def validate(self, data): #is_valid에서 검증하는 것
    #     print(data) #ordered dic: [('username', 'tulip3'), ('password', '1234'), ('email', 'tulip1@naver.com'), ('fullname', '한시원')]
    #     print(self.context.get("request", {}).method) #POST
    #     try:
    #         http_method = self.context.get["request"].method
    #     except:
    #         http_method = ''
    #     if http_method == "POST":

    #         if not data.get("email","").endswith("@naver.com"):
    #             raise serializers.ValidationError(
    #                 detail={"error": "네이버 이메일 혹은 지메일만 가입할 수 있습니다"}
    #             )
        
    #     return data

    class Meta:
        model = UserModel
        fields = ["username", "password", "email",
                  "fullname", "join_date",  "article", "comment", "userprofile"]

        extra_kwargs = {
            'password': {'write_only': True},
            'email': {
                'error_messages': {'required': '이메일을 입력해주세요', 'invalid': '알맞은 형식의 이메일을 입력해주세요'},
                'required': False
            },
        }
