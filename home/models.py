from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.AutoField(primary_key=True)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="profile_pic")

    def __str__(self):
        return f'{self.post_id}'


class Like(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post_id}'


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return f'{self.post_id}'
