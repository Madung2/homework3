from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

# Create your views here.


class ProductView(APIView):
    # 로그인 한 사용자의 게시글 목록 return

    # permission_classes = [permissions.TakesThreeMinutesToWrite]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({"message": "get입니다"})

    def post(self, request):
        return Response({"message": "post입니다"})

    def put(self, request):
        return Response({"message": "put입니다"})

    def delete(self, request):
        return Response({"message": "delete입니다"})
