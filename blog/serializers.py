from rest_framework import serializers
from .models import Post, Category, Tag

from django.contrib.auth.models import User, AnonymousUser


class CategorySerializer(serializers.ModelSerializer):
    """
    分类序列化
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    # article = serializers.ReadOnlyField(source='article.pk')

    class Meta:
        model = Category
        fields = ('id', 'name', 'is_nav', 'created_time', 'owner', 'article')


class NavSerializer(serializers.ModelSerializer):
    """
    分类序列化
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    # def update(self, instance, validated_data):
    #     print(instance)
    #     return instance

    # article = serializers.ReadOnlyField(source='article.pk')

    class Meta:
        model = Category
        fields = ('id', 'name', 'is_nav', 'created_time', 'owner', 'article')


class PostSerializer(serializers.ModelSerializer):
    """
    文章序列化
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    category_id = serializers.ReadOnlyField(source='category.id')
    comment = serializers.ReadOnlyField(source='comment.count')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Post
        fields = ('id', 'title', 'desc', 'content',
                  'status', 'category', 'tag', 'created_time', 'owner', 'is_md', 'content_html', 'comment',
                  'category_name', 'category_id')
        depth = 1


class TagSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Tag
        fields = ('id', 'name', 'owner', 'article',
                  'status', 'created_time')

# TODO 迁移到User目录 √
