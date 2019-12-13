from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from rest_framework import viewsets
from pprint import pprint
from .forms import CommentForm

# 评论集
from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(status=Comment.STATUS_NORMAL)

    def perform_create(self, serializer):
        is_anonymous = self.request.data.get('is_anonymous')
        print(self.request.data)
        if is_anonymous:
            user = User.objects.get(pk=3)
            serializer.save(owner=user)
        else:
            serializer.save(owner=self.request.user)

    def get_queryset(self):
        post = self.request.query_params.get('post', None)
        if post:
            queryset = Comment.objects.filter(status=Comment.STATUS_NORMAL, post=post).order_by('-created_time')
        else:
            queryset = Comment.objects.filter(status=Comment.STATUS_NORMAL).order_by('-created_time')

        return queryset
