from rest_framework import serializers

from appss.users.models import article


class ArticleSerialize(serializers.ModelSerializer):
    # title = serializers.CharField(required=True)
    # content = serializers.CharField(required=True)
    class Meta:
        model = article
        fields = ('id', 'title', 'content', 'ctime', 'mtime')