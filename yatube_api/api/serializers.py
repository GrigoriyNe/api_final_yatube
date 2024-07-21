from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import (
    Comment,
    Follow,
    Group,
    Post,
    User
)


User = get_user_model()


class AuthorMixin(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )


class PostSerializer(AuthorMixin):
    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(AuthorMixin):
    class Meta:
        fields = '__all__'
        read_only_fields = (
            'author',
            'post'
        )
        model = Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    def validate(self, data):
        if data['following'] == self.context['request'].user:
            raise serializers.ValidationError(
                "Dont subscribe on yourself"
            )
        return data

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following']
            )
        ]
