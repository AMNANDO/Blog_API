from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ('avatar', 'username', 'bio', 'role', 'email')

class RegisterUserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'role')

        def create(self, validated_data):
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
                role=validated_data('role', 'user'),
            )
            return user

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class UserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserDetailSerializer(UserSerializer):
    posts_count = serializers.IntegerField(read_only=True, source='posts.count')
    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('posts_count',)