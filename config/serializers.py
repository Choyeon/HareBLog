from rest_framework import serializers

from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Link
        fields = ["title", "href", "owner", "weight", "created_time"]
