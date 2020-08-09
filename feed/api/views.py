from rest_framework import viewsets

from rest_framework import generics

from feed.models import FeedItem

from feed.api.serializers import FeedItemSerializer

from rest_framework.permissions import IsAuthenticated

from feed.api.permissions import IFeedAuthorOrReadOnly


class FeedItemViewSet(viewsets.ModelViewSet):
    queryset = FeedItem.objects.all()
    serializer_class = FeedItemSerializer
    permission_classes = [ IsAuthenticated, IFeedAuthorOrReadOnly]


    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)