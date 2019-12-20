from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework_jwt.serializers import User

from blog.models import Tag, Post, Category
from blog.serializers import PostSerializer, CategorySerializer, TagSerializer, NavSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    获取全部博客
    """
    queryset = Post.latest_posts()
    serializer_class = PostSerializer
    search_fields = ('title', 'content', 'desc')
    filter_backends = (DjangoFilterBackend,)

    def perform_create(self, serializer):
        print(isinstance(self.request.user, User))
        # token = self.request.META.get('HTTP_AUTHORIZATION')
        # toke_user = jwt_decode_handler(token)
        # 获得user_id
        # user_id = toke_user["user_id"]
        # 通过user_id查询用户信
        # user_info = User.objects.get(pk=user_id)
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        search = self.request.query_params.get('search', None)
        if category:
            queryset = Post.objects.filter(status=Post.STATUS_NORMAL, category=category).order_by('-created_time')
            return queryset
        elif search:
            queryset = Post.objects.filter(status=Post.STATUS_NORMAL).order_by('-created_time')
            return queryset.filter(
                Q(title__icontains=search) | Q(desc__icontains=search) | Q(content__icontains=search))
        else:
            queryset = Post.objects.filter(status=Post.STATUS_NORMAL).order_by('-created_time')
            return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    """
    全部分类
    """
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL)
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NavViewSet(viewsets.ModelViewSet):
    """
    全部导航
    TODO rest framework 渲染器BUG显示有问题 目前无影响
    """
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL, is_nav=True)
    serializer_class = NavSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.filter(status=Tag.STATUS_NORMAL)
    serializer_class = TagSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
