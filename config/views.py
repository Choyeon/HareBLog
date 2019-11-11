from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from blog.views import CommonViewMixin

# Create your views here.
from config.models import Link


class LinkListView(CommonViewMixin, ListView):
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    template_name = 'config/links.html'
    context_object_name = 'link_list'

# TODO:今天完成评论功能
# TODO:一定要commit和push 🏁
# TODO:复习闭包
