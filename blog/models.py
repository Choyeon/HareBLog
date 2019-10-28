from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    这是分类的ORM模型类
    """
    STATUS_NORMAL = 1  # 正常状态
    STATUS_DELETE = 0  # 删除状态
    # 状态项目
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    # 分类名称
    name = models.CharField(max_length=50, verbose_name="名称")
    # 分类状态
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    # 是否是导航
    is_nav = models.BooleanField(default=False, verbose_name="是否为导航")
    # 作者的外键定义 指向'User'模型类 如果原作者被删除 则作者为空
    """
    on_delete 参数选项
    CASCADE:这就是默认的选项，级联删除，你无需显性指定它。
    PROTECT: 保护模式，如果采用该选项，删除的时候，会抛出ProtectedError错误。
    SET_NULL: 置空模式，删除的时候，外键字段被设置为空，前提就是blank=True, null=True,定义该字段的时候，允许为空。
    SET_DEFAULT: 置默认值，删除的时候，外键字段设置为默认值，所以定义外键的时候注意加上一个默认值。
    SET(): 自定义一个值，该值当然只能是对应的实体了
    """
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.SET_NULL)
    # 创建时间
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "分类"
