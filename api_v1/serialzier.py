
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tweet, Follow


class TweetSerilazer(serializers.ModelSerializer):

    class Meta:
        model = Tweet
        fields = ["id","user","text","image","created_at"]
        read_only_fields = ('user',)
        extra_kwargs = {"image": {"required": False, "allow_null": True}}



class FolloweSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = ["id", "user","target"]
        read_only_fields = ('user',)
