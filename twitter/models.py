from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tweet(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    liked_users = models.ManyToManyField(User, blank=True, related_name='likes_count', through='LikeTweet')
    disliked_users = models.ManyToManyField(User, blank=True, related_name='dislikes_count', through='DislikeTweet')

    def __str__(self):
        return f'{self.user.username} - {self.text}'



class Comment(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comm_user')
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    liked_users = models.ManyToManyField(User, blank=True, related_name='likes_count_comm', through='LikeComm')
    disliked_users = models.ManyToManyField(User, blank=True, related_name='dislikes_count_comm', through='DislikeComm')



    def __str__(self):
        return f'{self.text} - {self.tweet}'


class LikeTweet(models.Model):
    like_ch = (
        ('like', 'Like'),
    )
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.CharField(choices=like_ch, max_length=10)
    liked_at = models.DateField(auto_now_add=True)


class DislikeTweet(models.Model):
    dislike_ch = (
        ('dislike', 'Dislike'),
    )
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.CharField(choices=dislike_ch, max_length=10)
    disliked_at = models.DateField(auto_now_add=True)


class LikeComm(models.Model):
    like_comm = (
        ('like', 'Like'),
    )
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.CharField(choices=like_comm, max_length=10)
    liked_at = models.DateField(auto_now_add=True)


class DislikeComm(models.Model):
    dislike_comm = (
        ('dislike', 'DisLike'),
    )
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.CharField(choices=dislike_comm, max_length=10)
    liked_at = models.DateField(auto_now_add=True)
