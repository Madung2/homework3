from rest_framework import serializers
from product.models import Product as ProductModel
from product.models import Review as ReviewModel
from django.utils.timezone import localdate, timezone
import datetime as dt
from django.utils import timezone


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()  # 유저시리얼라이저 안 씀

    def get_user(self, obj):

        return obj.user.username

    class Meta:
        model = ReviewModel
        fields = ['user', 'product', 'contents', 'posting_date', ]


class ProductSerializer(serializers.ModelSerializer):

    def validate(self, data):  # is_valid에서 검증하는 것

        # print(data) #ordered dic: [('user', <User: tulip / tuliphan91@gmail.com / 한예슬>), ('title', '4번 업데이트'), ('thumbnail', <InMemoryUploadedFile: 00000.png (image/png)>), ('contents', '이런저런 이런절ㄴ 이런 프로덕트 입니다!!!하핫1'), ('expire_date', datetime.datetime(2022, 8, 30, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC'))), ('cost', 50000), ('is_active', False)]
        # print(data.get("expire_date")) #2022-08-30 00:00:00+00:00
        # expire_date = data.get("expire_date")
        # print(type(expire_date)) #논타입
        # print(timezone.now()) # 2022-06-23 17:23:47.827962
        # print(data.get("expire_date")-timezone.now()) # 67 days, 13:22:37.705211
        if data.get("expire_date"):
            if data.get("expire_date") < timezone.now():
                raise serializers.ValidationError(
                    detail={"error": "노출 종료 일자가 현재보다 이전입니다"})
        return data

    def create(self, validated_data):
        contents = validated_data.pop("contents")
        # print(contents)
        validated_data['contents'] = f'{contents}{timezone.now()}에 등록된 상품입니다'
        # print(validated_data)
        return ProductModel.objects.create(**validated_data)

    def update(self, instance, validated_data):  # 인스턴스에는 입력된 object가 담긴다
        # print(f'instan=>{instance}')  # 3번 업데이트 입니다.(기존정보)
        # print(f'vali=>{validated_data}')  # {'title': '3번이라'}(나중정보)
        # print(instance.contents)
        instance.contents = f'{timezone.now()}에 수정되었습니다.' + instance.contents
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
                continue
            setattr(instance, key, value)

        return instance

    # reviews = ReviewSerializer(many=True, source="review_set", read_only=True)
    reviews = serializers.SerializerMethodField()  # 유저시리얼라이저 안 씀

    def get_reviews(self, obj):
        if obj:
            review_first = obj.review_set.all().first()
            return {"reviews": ReviewSerializer(review_first).data}
        else:
            return {}

    class Meta:
        model = ProductModel
        fields = ['user', 'title', 'thumbnail', 'contents', 'posting_date',
                  'expire_date', 'cost', 'updated_at', 'is_active', 'reviews']
