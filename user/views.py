from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework import viewsets, status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from django.http import JsonResponse

from .serializers import UserRegSerializer, UserSerializer

User = get_user_model()  # 从settings里面去找用户认证模型类 Django.contrib.auth里自带的方法


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """

    # todo BUG解决 加request  官方文档 https://docs.djangoproject.com/en/1.11/topics/auth/customizing/
    # todo 博客地址 http://www.pythonheidong.com/blog/article/157431/

    def authenticate(self, request, username=None, password=None, **kwargs):
        print("认证+++++++++++++++++++++++++++++++", request, kwargs)
        try:
            # 用户名和邮箱都能登录
            user = User.objects.get(
                Q(username=username) | Q(email=username)
            )
            print("-----------------------------------", user)
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# http://127.0.0.1:8000/api/user/register
# 用户注册 继承create视图集
class UserViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
      用户
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.username

        headers = self.get_success_headers(serializer.data)

        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
