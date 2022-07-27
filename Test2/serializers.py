from rest_framework import serializers

from .models import Post2, Comment2

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post2
        fields = '__all__'

    def to_representation(self, instance):
        dict_ = super().to_representation(instance)
        dict_['user'] = instance.user.username
        dict_['comments2'] = CommentSerializer(instance.comments.all(), many=True).data
        return dict_

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment2
        exclude = ['post2']

    def to_representation(self, instance):
        dict_ = super().to_representation(instance)
        dict_['user'] = instance.user.username
        return dict_