from django.contrib.auth.models import User
from django.db import models
from django.template.loader import render_to_string


class Link(models.Model):
    """
    友情链接
    """
    STATUS_NORMAL = 1  # 正常状态
    STATUS_DELETE = 0  # 删除状态
    # 状态项目
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    # link标题
    title = models.CharField(max_length=50, verbose_name="标题")
    # link url
    href = models.URLField(verbose_name="链接")
    # 链接状态
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    # 权重
    weight = models.PositiveIntegerField(default=1,
                                         choices=zip(range(1, 6),
                                                     range(1, 6)),
                                         verbose_name="权重",
                                         help_text="权重高展示顺序靠前")
    # 作者的外键定义 指向'User'模型类 如果原作者被删除 则作者为空
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    # 创建时间
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "友情链接"


class SideBar(models.Model):
    # 显示状态
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, "展示"),
        (STATUS_HIDE, "隐藏"),
    )
    # 侧栏类型
    DISPLAY_HTML = 1
    DISPLAY_LATEST = 2
    DISPLAY_HOT = 3
    DISPLAY_COMMENT = 4
    SIDE_TYPE = (
        (DISPLAY_HTML, "HTML"),
        (DISPLAY_LATEST, "最新文章"),
        (DISPLAY_HOT, "最热文章"),
        (DISPLAY_COMMENT, "最近评论"),
    )
    # 侧栏标题
    title = models.CharField(max_length=50, verbose_name="标题")
    # 侧栏类型
    display_type = models.PositiveIntegerField(default=1, choices=SIDE_TYPE, verbose_name=" 展示类型")
    # 侧栏展示内容
    content = models.CharField(max_length=500, verbose_name="展示内容", blank=True, help_text="如果不是HTML类型可为空")
    # 状态
    status = models.PositiveIntegerField(default=STATUS_SHOW, choices=STATUS_ITEMS, verbose_name="状态")
    # 作者的外键定义 指向'User'模型类
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    # 创建时间
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "侧边栏"

    @classmethod
    def get_all(cls):
        """
        :return:全部内容
        """
        return cls.objects.filter(status=cls.STATUS_SHOW)

    @property
    def content_html(self):
        """直接渲染模版"""

        # 避免循环引用
        from blog.models import Post
        from comment.models import Comment

        result = ''
        if self.display_type == self.DISPLAY_HTML:
            result = self.content
        elif self.display_type == self.DISPLAY_LATEST:
            context = {
                'posts': Post.latest_posts()
            }
            result = render_to_string('config/blocks/sidebar_posts.html', context)
        elif self.display_type == self.DISPLAY_HOT:
            context = {
                'posts': Post.hot_posts()
            }
            result = render_to_string('config/blocks/sidebar_posts.html', context)

        elif self.display_type == self.DISPLAY_COMMENT:
            context = {
                'comments': Comment.objects.filter(status=Comment.STATUS_NORMAL)
            }
            result = render_to_string("config/blocks/sidebar_comments.html", context)
        return result

    def __str__(self):
        return self.title
