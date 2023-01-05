from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from twitter import views

router = routers.DefaultRouter()
router_mark = routers.DefaultRouter()
router.register('tweet', views.TweetViewSet)
router.register('comment', views.CommentViewSet)
router.register('like', views.LikeViewSet)
router.register('dislike', views.DislikeViewSet)
router.register('likecomm', views.LikeCommViewSet)
router.register('dislikecomm', views.DislikeCommViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v-1.0/', include(router.urls))
]
