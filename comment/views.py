from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from rest_framework import viewsets
from pprint import pprint

from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication, jwt_decode_handler

from .forms import CommentForm

# 评论集
from .models import Comment
from .serializers import CommentSerializer


# TODO 拆分 使post请求限流
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(status=Comment.STATUS_NORMAL)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def perform_create(self, serializer):
        is_anonymous = self.request.data.get('is_anonymous')
        if is_anonymous:
            user = User.objects.get(pk=3)
            serializer.save(owner=user)
        else:
            token = self.request.META.get('HTTP_AUTHORIZATION')
            toke_user = jwt_decode_handler(token)
            # 获得user_id
            user_id = toke_user["user_id"]
            # 通过user_id查询用户信
            user_info = User.objects.get(pk=user_id)
            serializer.save(owner=user_info, nickname=user_info.username, email=user_info.email,
                            website='http://www.com')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        print(serializer.data, type(serializer.data))

        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        post = self.request.query_params.get('post', None)
        if post:
            queryset = Comment.objects.filter(status=Comment.STATUS_NORMAL, post=post).order_by('-created_time')
        else:
            queryset = Comment.objects.filter(status=Comment.STATUS_NORMAL).order_by('-created_time')

        return queryset
