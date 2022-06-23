from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from product.models import Product as ProductModel
from product.serializers import ProductSerializer
from datetime import datetime
# Create your views here.


class ProductView(APIView):
    # 로그인 한 사용자에게 물건 보이기

    # permission_classes = [permissions.TakesThreeMinutesToWrite]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        today = datetime.now()
        products = ProductModel.objects.filter(
            posting_date__lte=today, expire_date__gte=today).filter(user=request.user)
        product = [product.title for product in products]  # list 축약 문법

        return Response({"product": product})

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
