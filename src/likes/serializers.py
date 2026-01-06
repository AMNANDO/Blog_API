from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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

    def validate(self, attrs):
        request = self.context['request']
        post = self.context['post']

        if Like.objects.filter(post=post, user=request.user).exists():
            raise ValidationError('You are already liked this post.')
        return attrs

    def create(self, validated_data):
        request = self.context['request']
        post = self.context['post']

        return Like.objects.create(
            user=request.user,
            post=post,
        )