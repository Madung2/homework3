from rest_framework import serializers
from blog.models import Article as ArticleModel
from blog.models import Comment as CommentModel
from blog.models import Category as CategoryModel


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = ['name']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()  # 유저시리얼라이저 안 씀

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = CommentModel
        fields = ['user', 'contents']


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()  # 시리얼라이즈메소드필드도 기본적으로 read only
    # many=True는 여러개를 나열할때, 역참조라 포스트할때 불필요하니까 read only=True
    comments = CommentSerializer(
        many=True, source="comment_set", read_only=True)
    # 모델상에는 comment가 article에 연결이 되어 있어서

    def get_category(self, obj):
        return [category.name for category in obj.category.all()]

    class Meta:
        model = ArticleModel
        # 모델에 있는거 다 들어 있어야함.
        fields = ['user', 'category', 'title', 'contents',
                  'comments', "posting_date", "expire_date"]
