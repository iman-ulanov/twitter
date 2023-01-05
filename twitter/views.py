from rest_framework import viewsets, authentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Tweet, Comment, LikeTweet, DislikeTweet, LikeComm, DislikeComm
from .permissions import IsTweetOwner
from .serializers import TweetSerializer, CommentSerializer, LikeSerializer, \
    DislikeSerializer, LikeCommSerializer, DislikeCommSerializer


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [IsTweetOwner]



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer,
#
#     authentication_classes = [authentication.BasicAuthentication]

class LikeViewSet(viewsets.ModelViewSet):
    queryset = LikeTweet.objects.all()
    serializer_class = LikeSerializer
    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [IsAuthenticatedOrReadOnly]

    # def isliked(self, request):
    #     exists = LikeTweet.objects.order_by('id').values()
    #     if request.method == "POST":
    #         if self.request.user in exists:
    #             return f"Вы уже лайкнули пост"


class DislikeViewSet(viewsets.ModelViewSet):
    queryset = DislikeTweet.objects.all()
    serializer_class = DislikeSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class LikeCommViewSet(viewsets.ModelViewSet):
    queryset = LikeComm.objects.all()
    serializer_class = LikeCommSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class DislikeCommViewSet(viewsets.ModelViewSet):
    queryset = DislikeComm.objects.all()
    serializer_class = DislikeCommSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)
