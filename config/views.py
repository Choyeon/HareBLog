# Create your views here.
from rest_framework import viewsets
from .models import Link
from .serializers import LinkSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL).order_by('-weight')
    serializer_class = LinkSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)