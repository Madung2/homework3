from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField("이름", max_length=50)
    description = models.TextField("설명")

    def __str__(self):
        return self.name


class Article(models.Model):
    user = models.ForeignKey(
        'user.User', verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50)
    category = models.ManyToManyField(Category, verbose_name="카테고리")
    contents = models.TextField("본문")
    posting_date = models.DateTimeField("노출시작일", auto_now_add=True)
    expire_date = models.DateTimeField("노출 종료 일자", default=timezone.now)

    def __str__(self):
        return f"{self.user.username} 님이 작성하신 글입니다."


class Comment(models.Model):
    
    article = models.ForeignKey(
        Article, verbose_name="원글", on_delete=models.CASCADE)
    user = models.ForeignKey(
        'user.User', verbose_name="작성자", on_delete=models.CASCADE)
    content = models.TextField("댓글 내용")

    def __str__(self):
        return f"{self.user.username} 님 댓글입니다."
