from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'category', 'article', 'password', 'tag')


class UserRegSerializer(serializers.ModelSerializer):
    """
    用户注册
    """
    # 验证用户名是否存在
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])
    # 注册时默认用户为匿名用户 直接修改序列化文件使账号可用
    is_active = serializers.BooleanField(default=True)

    # 密码加密保存 重写create方法
    def create(self, validated_data):
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        print(user.is_active)
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = "__all__"
