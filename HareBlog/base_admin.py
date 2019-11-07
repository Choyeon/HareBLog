from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    """
    用来补充文章  分类 侧边栏 友情链接这些model的owner字段
    用来针对queryset 过滤当前用户数据
    """
    exclude = ('owner',)

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)
