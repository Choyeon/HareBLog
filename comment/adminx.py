import xadmin
from django.contrib import admin

from HareBlog.base_admin import BaseOwnerAdmin
from .models import Comment


@xadmin.sites.register(Comment)
class CommentAdmin(object):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
