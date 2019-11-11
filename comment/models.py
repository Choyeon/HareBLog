from django.db import models

from blog.models import Post


class Comment(models.Model):
    """
    评论
    """
    STATUS_NORMAL = 1  # 正常状态
    STATUS_DELETE = 0  # 删除状态
    # 状态项目
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    # 评论目标链接到Post文章发布模型类
    target = models.CharField(max_length=100, verbose_name="评论目标")
    # 评论内容
    content = models.CharField(max_length=2000, verbose_name="内容")
    # 昵称
    nickname = models.CharField(max_length=50, verbose_name="昵称")
    # 网站URL
    website = models.URLField(verbose_name="网站")
    # 邮箱地址
    email = models.EmailField(verbose_name="邮箱")
    # 评论状态
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    # 创建时间
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "评论"

    @classmethod
    def get_by_target(cls, target):
        return cls.objects.filter(target=target, status=Comment.STATUS_NORMAL)

