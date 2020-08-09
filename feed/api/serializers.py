from rest_framework import serializers

from feed.models import FeedItem


class FeedItemSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()


    class Meta:
        model = FeedItem
        fields = ('id', 'user', 'status', 'updated_at', 'created_at')


    def get_created_at(self, object):
        created_at = object.created_at
        return created_at.strftime("%B %d, %Y")

    def get_updated_at(self, instance):
        return instance.updated_at.strftime("%B %d, %Y")