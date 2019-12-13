from rest_framework import serializers

from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'nickname', 'website', 'email', 'status', 'owner', 'created_time',
                  'is_anonymous', 'like']
