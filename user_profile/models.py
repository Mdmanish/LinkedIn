from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='profile_pic/default_cover_pic.jpeg', null=True, blank=True, upload_to="profile_pic")
    cover_image = models.ImageField(
        default='profile_pic/default_cover_pic.jpeg', null=True, blank=True, upload_to="profile_pic")
    bio = models.TextField(default='SDE')
    company = models.CharField(default='MountBlue', max_length=200)
    about = models.TextField(default='about')

    def __str__(self):
        return f'{self.user.username}'


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='profile_pic/default_exp_img.png', null=True, blank=True, upload_to="profile_pic")
    title = models.CharField(default='title', max_length=200)
    company = models.CharField(default="company", max_length=200)
    job_type = models.CharField(default="full-time", max_length=200)
    joining_date = models.CharField(default="Jan 2021", max_length=200)
    leaving_date = models.CharField(default="Present", max_length=200)
    duration = models.CharField(default="2.5 years", max_length=200)
    description = models.TextField(default="discription")

    def __str__(self):
        return f'{self.user.username}'


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='profile_pic/lpu.jpeg', null=True, blank=True, upload_to="profile_pic")
    college = models.CharField(default="LPU", max_length=300)
    course = models.CharField(default="B.Tech, CSE", max_length=300)
    starting_date = models.CharField(default="July 2019", max_length=200)
    end_date = models.CharField(default="Present", max_length=200)

    def __str__(self):
        return f'{self.user.username}'


class Certificates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='profile_pic/default_cover_pic.jpeg', null=True, blank=True, upload_to="profile_pic")
    title = models.CharField(default='title', max_length=200)
    organisation = models.CharField(default="organisation", max_length=200)
    issue_date = models.CharField(default="Jan 2021", max_length=200)
    expiry_date = models.CharField(
        default="No Expiration Date", max_length=200)

    def __str__(self):
        return f'{self.user.username}'


class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(default="DSA", max_length=200)


class Languages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(default="English", max_length=100)


class Followers(models.Model):
    user = models.CharField(max_length=100)
    follower = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user}'


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    reciver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reciver")
    value = models.CharField(max_length=1111)
    date = models.DateTimeField(default=datetime.now, blank=True)
