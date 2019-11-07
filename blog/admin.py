from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin.models import LogEntry

from .adminforms import PostAdminForm
from .models import Category, Tag, Post
from HareBlog.custom_site import custom_site
from HareBlog.base_admin import BaseOwnerAdmin


class PostInline(admin.TabularInline):
    # fields = {'title', 'desc'}
    extra = 1
    model = Post


# 分类的admin
@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline, ]
    # 列表显示
    list_display = ('name', 'status', 'is_nav', 'created_time')
    # 领域
    fields = ('name', 'status', 'is_nav')


# 标签的admin
@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    # 列表显示、
    list_display = ('name', 'status', 'created_time')
    # 领域
    fields = ('name', 'status')


class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器类"""
    title = "分类过滤器"
    parameter_name = "owner_category"

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


class TagFilter(admin.SimpleListFilter):
    title = "标签过滤器"
    parameter_name = "tag"

    def lookups(self, request, model_admin):
        return Tag.objects.all().values_list('id', 'name')

    def queryset(self, request, queryset):
        tag_id = self.value()
        if tag_id:
            return queryset.filter(tag=self.value())
        return queryset


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'title', 'category', 'status',
        'created_time', 'operator', 'owner'
    ]

    fieldsets = (
        ('基础设置', {'description': '基础配置描述',
                  'fields': (('title', 'category'),
                             'status',
                             ),
                  }),
        ('内容', {
            'fields': (
                'desc',
                'content',
            ),
        }),
        ('额外信息', {
            'classes': ('wide',),
            'fields': ('tag',),
        })
    )
    list_display_links = []

    list_filter = [CategoryOwnerFilter, TagFilter]
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    # 编辑
    save_on_top = True

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = "操作"

    class Media:
        css = {
            # 'all': ('https://cdn.bootcss.com/twitter-bootstrap/4.0.0/css/bootstrap.css',)
        }
        js = ('https://cdn.bootcss.com/twitter-bootstrap/4.3.1/js/bootstrap.bundle.js',)


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']
