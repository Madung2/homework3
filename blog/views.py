from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from blog.models import Article as ArticleModel
from blog.models import Category as CategoryModel

from ai.permissions import TakesThreeMinutesToWrite

# path('article/',
class ArticleView(APIView):
    # 로그인 한 사용자의 게시글 목록 return
    # 
    
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        
        articles = ArticleModel.objects.filter(user=user)
        titles = [article.title for article in articles] # list 축약 문법

        titles = []

        for article in articles:
            titles.append(article.title)

        return Response({"article_list": titles})

    permission_classes = [TakesThreeMinutesToWrite]
    def post(self, request):
        user= request.user
        contents = request.data.get('contents','')  #request.POST.get
        title = request.data.get('title','')
        category = request.data.get('category', '')
        # print(len(contents))
        # print(len(category))
        # print(len(title))

        if len(title) <6 or len(contents) <21:
            return Response({"message":"게시글을 작성할 수 없습니다"})
        if not category:
            return Response({"message":"카테고리를 지정해야 합니다"})
        categories = [CategoryModel.objects.get(name=category)]
        # print(categories) # [<Category: 로맨스>]
            
        my_article = ArticleModel.objects.create(user= user, contents=contents, title=title)
        my_article.category.add(*categories)
        my_article.save()

        return Response({"message":"article"})

