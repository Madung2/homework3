from importlib.resources import contents
from itertools import product
from multiprocessing import AuthenticationError
from tabnanny import verbose
from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(
        'user.User', verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50)
    thumbnail = models.FileField(upload_to='uploads/', verbose_name="썸네일")
    contents = models.TextField("상품 설명")
    posting_date = models.DateTimeField(auto_now_add=True, verbose_name="등록일자")
    expire_date = models.DateTimeField(default=timezone.now, verbose_name="노출 종료 일자")
    cost = models.IntegerField("가격")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정 일자")
    is_active = models.BooleanField(default=True, verbose_name="활성화 여부")


    def __str__(self):
        return f"{self.title} 입니다."
    
    
class Review(models.Model):
    user = models.ForeignKey("user.User", verbose_name="작성자", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="상품", on_delete=models.CASCADE)
    contents = models.TextField("리뷰 내용")
    posting_date = models.DateTimeField(auto_now_add=True, verbose_name="작성일")