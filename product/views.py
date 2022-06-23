from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from product.models import Product as ProductModel
from product.models import Review as ReviewModel
from product.serializers import ProductSerializer
from product.serializers import ReviewSerializer
from datetime import datetime
from django.db.models import Q
# Create your views here.
# from ai.permissions import ThreeDayUserCanWrite


class ProductView(APIView):
    # 로그인 한 사용자에게 물건 보이기

    # permission_classes = [permissions.TakesThreeMinutesToWrite]
    # permission_classes = [ThreeDayUserCanWrite]

    # permission_classes =[permissions.AllowAny]
    def get(self, request):
        today = datetime.now()
        products = ProductModel.objects.filter(
            (Q(posting_date__lte=today, expire_date__gte=today) | Q(user=request.user))
            & Q(is_active=True))
        # product = [product.title for product in products]  # list 축약 문법

        # return Response({"product": product})
        product_serializer = ProductSerializer(products, many=True)


        return Response(product_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        request.data['user'] = user.id
        product_serializer = ProductSerializer(data=request.data)

        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)

        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, obj_id):
        product = ProductModel.objects.get(id=obj_id)
        print(obj_id)
        # 수정할땐 어떤걸 수정할지를 앞에 지정해야함.
        product_serializer = ProductSerializer(
            product, data=request.data, partial=True)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, obj_id):
    #     event = ProductModel.objects.get(id=obj_id)
    #     event.delete()
    #     return Response(, status=status.HTTP_200_OK)


class ReviewView(APIView):
    def get(self, request):
        reviews = ReviewModel.objects.all()
        return Response(ReviewSerializer(reviews, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({"message": "post입니다"})

    def put(self, request):
        return Response({"message": "put입니다"})

    def delete(self, request):
        return Response({"message": "delete입니다"})
