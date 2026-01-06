from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id', 'author', 'created_at', 'updated_at', 'is_active', 'status')

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'status')

    def create(self, validated_data):
        request = self.context.get['request']
        validated_data['author'] = request.user
        return Post.objects.create(**validated_data)

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'status')

        def validate(self, attrs):
            if self.instace.status != "published" and attrs.get('status') == "published":
                pass
            return attrs

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id', 'author', 'created_at', 'updated_at', 'is_active', 'status')

class PostAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'