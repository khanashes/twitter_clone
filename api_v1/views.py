from django.contrib.auth.models import User
from rest_framework import mixins, serializers, viewsets
from rest_framework import permissions
from rest_framework.response import Response
from django.http import Http404, request
from rest_framework import status
from .models import Tweet, Follow
from .serialzier import FolloweSerializer, TweetSerilazer, Follow
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
# Create your views here.

'''
Post tweet/ to post a tweet
Get tweet/ to get tweets of followers and their own
Delete tweet/ to delete the tweet
Put tweet/ to update the tweet
Patch tweet/ to partially update
'''
class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerilazer
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        user_tweets = self.request.user.tweets.all()
        follows = self.request.user.friends.all()
        for follow in follows:
            user_tweets = user_tweets | self.queryset.filter(user=follow.target)
        return user_tweets
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def destroy(self, request, *args, **kwargs):
        # object level permission checking
        tweet = self.get_object()
        tweet.delete()
        return Response(data='Deleted')

    def update(self, request, *args, **kwargs):
        tweet = self.get_object()
        tweet.delete()
        return Response(data='updated')

    def partial_update(self, request, *args, **kwargs):
        tweet = self.get_object()
        tweet.delete()
        return Response(data='partially updated')

'''
post follow/ to follow the user
delete follow/ to unfollow the user
get follow/ to get list of followers
'''
class FollowView(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = FolloweSerializer
    queryset = Follow.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except Exception as e:
            raise Custom409(e.__str__())


# Custom exception handling when unique contraint exception arise
class Custom409(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "You can't follow again"