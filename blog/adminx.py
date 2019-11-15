import xadmin
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin.models import LogEntry

from xadmin.layout import Row, Fieldset, Container
from xadmin.filters import RelatedFieldListFilter, manager

from .adminforms import PostAdminForm
from .models import Category, Tag, Post
from HareBlog.custom_site import custom_site
from HareBlog.base_admin import BaseOwnerAdmin


class PostInline:
    form_layout = (
        Container(
            Row("title", "desc"),
        )
    )
    extra = 1  # 控制额外多几个
    model = Post


# 分类的admin
@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    # inlines = [PostInline, ]
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


# 标签的admin
class TagAdmin(BaseOwnerAdmin):
    # 列表显示、
    list_display = ('name', 'status', 'created_time')
    # 领域
    fields = ('name', 'status')


class CategoryOwnerFilter(RelatedFieldListFilter):
    """自定义过滤器类"""

    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'

    def __init__(self, field, request, params, model, admin_view, field_path):
        super().__init__(field, request, params, model, admin_view, field_path)
        self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id', 'name')


manager.register(CategoryOwnerFilter, take_priority=True)


@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'title', 'category', 'status',
        'created_time', 'operator', 'owner'
    ]

    form_layout = (
        Fieldset(
            "基础信息",
            Row('title', 'category'),
            'status',
            'tag'
        ),
        Fieldset(
            '内容信息',
            'desc',
            'content'
        )
    )

    list_display_links = []

    list_filter = ['category']
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    # 编辑
    save_on_top = True

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('xadmin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = "操作"

    class Media:
        css = {
            'all': ('https://cdn.bootcss.com/twitter-bootstrap/4.0.0/css/bootstrap.css',)
        }
        js = ('https://cdn.bootcss.com/twitter-bootstrap/4.3.1/js/bootstrap.bundle.js',)
