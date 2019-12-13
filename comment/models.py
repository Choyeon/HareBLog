from django.db import models

from blog.models import Post
from django.contrib.auth.models import User


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
    post = models.ForeignKey(Post, max_length=100, verbose_name="评论目标", on_delete=models.CASCADE,
                             related_name='comment')
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
    # 评论的用户
    owner = models.ForeignKey(User, verbose_name='发布者', on_delete=models.CASCADE, related_name='comment', default=None)
    # 创建时间ß
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 是否为匿名评论
    is_anonymous = models.BooleanField(default=True, verbose_name='匿名用户')
    like = models.IntegerField(default=0, verbose_name='点赞数')

    class Meta:
        verbose_name = verbose_name_plural = "评论"
        db_table = 'comment'

    def __str__(self):
        return self.content

    def new_comment(self):
        self.objects.filter(status=self.STATUS_NORMAL).order_by('created_time')


class CommentReply(models.Model):
    reply_to = models.ForeignKey(Comment, verbose_name='回复到到评论', related_name='reply_to', on_delete=models.CASCADE)
    reply = models.ForeignKey(Comment, verbose_name="恢复到评论", related_name="reply", on_delete=models.CASCADE)
