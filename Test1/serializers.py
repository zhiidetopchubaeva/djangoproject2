from rest_framework import serializers

from .models import Post1, Comment1

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post1
        fields = '__all__'

    def to_representation(self, instance):
        dict_ = super().to_representation(instance)
        dict_['user'] = instance.user.username
        dict_['comments1'] = CommentSerializer(instance.comments.all(), many=True).data
        return dict_

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment1
        exclude = ['post1']

    def to_representation(self, instance):
        dict_ = super().to_representation(instance)
        dict_['user'] = instance.user.username
        return dict_