from rest_framework import routers
from .views import TweetViewSet, FollowView
from rest_framework.routers import DefaultRouter
from django.urls import path
router = DefaultRouter()
router.register(r'tweet', TweetViewSet, basename="tweet")
router.register(r'follow', FollowView, basename="follow")
urlpatterns  = router.urls
