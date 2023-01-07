from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Lead(models.Model):
    # CHANNELS = (("YT", "Youtube"), ("GO", "Google")("NL", "Newsletter"))
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True)
    # isContacted = models.BooleanField(default=False)
    # channel = models.CharField(choices=CHANNELS, max_length=100)
    # profile_picture = models.ImageField(blank=True, null=True)
    # files = models.FileField(blank=True, null=True)


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
