from rest_framework import viewsets
from blog.models import Tag, Post, Category
from blog.serializers import PostSerializer, CategorySerializer, UserSerializer, TagSerializer, NavSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    获取全部博客
    """
    queryset = Post.latest_posts()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL)
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NavViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL, is_nav=True)
    serializer_class = NavSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.filter(status=Tag.STATUS_NORMAL)
    serializer_class = TagSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
