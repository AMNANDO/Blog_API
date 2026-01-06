from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Like
        fields = ('id', 'user', 'created_at')

class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ()

    def create(self, validated_data):
        request = self.context['request']
        post = self.context['post']

        return Like.objects.create(
            user=request.user,
            post=post,
        )