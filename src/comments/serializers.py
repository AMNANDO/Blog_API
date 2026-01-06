from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'id', 'is_active', 'created_at')

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',)

        def validate(self, attrs):
            request = self.context['request']
            post = self.context['post']

            comments_count = Comment.objects.filter(post=post, author=request.user).count()

            if comments_count >= 10:
                raise serializers.ValidationError('You cannot add more than 10 comments to this post')
            return attrs

        def create(self, validated_data):
            request = self.context['request']
            post = self.context['post']

            try:
                return Comment.objects.create(post=post,
                                              author=request.user,
                                              content=validated_data['content']
                )
            except ValidationError as e:
                raise serializers.ValidationError(e.message_dict)
