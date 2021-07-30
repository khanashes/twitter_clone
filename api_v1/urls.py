from .views import TweetViewSet, FollowView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.urls import path
router = DefaultRouter()
router.register(r'tweet', TweetViewSet, basename="tweet")
router.register(r'follow', FollowView, basename="follow")
urlpatterns  = router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
