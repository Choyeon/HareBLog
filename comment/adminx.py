import xadmin

from .models import Comment


@xadmin.sites.register(Comment)
class CommentAdmin:
    list_display = ('post', 'nickname', 'content', 'website', 'created_time')
