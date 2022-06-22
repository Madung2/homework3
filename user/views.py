from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from django.contrib.auth import login, logout, authenticate
from user.serializers import UserSerializer
from user.models import User as UserModel


class UserView(APIView):
    permission_classes = [permissions.AllowAny]

    # 사용자 정보 조회
    def get(self, request):
        # user = request.user
        # return Response(UserSerializer(user).data)
        user_serializer = UserSerializer(request.user, context={"request":request}).data
        return Response(user_serializer, status=status.HTTP_200_OK)

    # 회원가입
    def post(self, request):
        user_serializer = UserSerializer(data=request.data, context={"request":request})
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 회원 정보 수정
    def put(self, request, obj_id):
        #오브젝트 아이디로 불러오면 다른 사람꺼 수정할 수 있으니깐...
        print(obj_id)
        
        user_id=request.user.id
        print(user_id)
        #request.pop('username','') <=유저네임은 수정하지 않게 하고 싶다
        user = UserModel.objects.get(id=user_id)
        user_serializer = UserSerializer(user, data= request.data, partial=True) #수정할땐 어떤걸 수정할지를 앞에 지정해야함.
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    # 회원 탈퇴
    def delete(self, request):
        return Response({"message": "delete method!!"})

class UserAPIView(APIView):
    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)

        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."})

        login(request, user)
        return Response({"message": "login success!!"})
    
    def delete(self, request):
        logout(request)
        return Response({"message": "logout success!!"})
