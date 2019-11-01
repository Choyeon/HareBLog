from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Category, Tag, Post


# 分类的admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # 列表显示
    list_display = ('name', 'status', 'is_nav', 'created_time')
    # 领域
    fields = ('name', 'status', 'is_nav')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


# 标签的admin
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # 列表显示、
    list_display = ('name', 'status', 'created_time')
    # 领域
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


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


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'category', 'status',
        'created_time', 'operator', 'owner'
    ]
    list_display_links = []

    list_filter = [CategoryOwnerFilter, TagFilter]
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    # 编辑
    save_on_top = True

    fields = (
        ('category', 'title'),
        'desc',
        'status',
        'content',
        'tag'
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = "操作"

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)
