from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from blog.models import Article as ArticleModel
from blog.models import Category as CategoryModel
from datetime import datetime
from blog.serializers import ArticleSerializer
from ai.permissions import TakesThreeMinutesToWrite
from django.utils import timezone

# path('article/',


class ArticleView(APIView):
    # 로그인 한 사용자의 게시글 목록 return

    # permission_classes = [permissions.TakesThreeMinutesToWrite]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        user = request.user
        today = timezone.now()

        articles = ArticleModel.objects.filter(
            user=user, expire_date__gt=datetime.now()).order_by('-id')
        titles = [article.title for article in articles]  # list 축약 문법

        return Response({"titles": titles})

    def post(self, request):
        user = request.user
        request.data['user'] = user.id
        article_serializer = ArticleSerializer(data = request.data)
        if article_serializer.is_valid():
            article_serializer.save()
            return Response(article_serializer.data, status=status.HTTP_200_OK)
        return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        '''
        여기는 시리얼라이저를 사용하지 않는 방식
        '''
        # user = request.user
        # contents = request.data.get('contents', '')  # request.POST.get
        # title = request.data.get('title', '')
        # category = request.data.get('category', '')
        # posting_date = request.data.get('posting_date')
        # expire_date = request.data.get('expire_date')
        # # print(len(contents))
        # # print(len(category))
        # # print(len(title))

        # if len(title) < 6 or len(contents) < 11:
        #     return Response({"message": "게시글을 작성할 수 없습니다"})
        # if not category:
        #     return Response({"message": "카테고리를 지정해야 합니다"})
        # categories = [CategoryModel.objects.get(name=category)]
        # # print(categories) # [<Category: 로맨스>]

        # my_article = ArticleModel.objects.create(
        #     user=user, contents=contents, title=title, posting_date=posting_date, expire_date=expire_date)
        # my_article.category.add(*categories)
        # my_article.save()

        # return Response({"message": "article"})
