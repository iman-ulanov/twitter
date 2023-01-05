from rest_framework import serializers

from .models import Tweet, Comment, LikeTweet, DislikeTweet, LikeComm, DislikeComm, User


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"


class TweetSerializer(serializers.ModelSerializer):
    # total_likes = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = '__all__'
        read_only_fields = ['user']

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return attrs


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['user']

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return attrs


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeTweet
        fields = '__all__'

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return attrs


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DislikeTweet
        fields = '__all__'

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return attrs


class LikeCommSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeComm
        fields = '__all__'

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return attrs


class DislikeCommSerializer(serializers.ModelSerializer):
    class Meta:
        model = DislikeComm
        fields = '__all__'

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return attrs
