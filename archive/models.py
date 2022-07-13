from django.db import models

from django.contrib.auth.models import User
from leak.models import Leak, Image, Audio, File, Video
# Create your models here.


class Archive(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='archive')
    leaks = models.ManyToManyField(Leak, blank=True, related_name='archives')
    images = models.ManyToManyField(Image, blank=True, related_name='archives')
    audios = models.ManyToManyField(Audio, blank=True, related_name='archives')
    files = models.ManyToManyField(File, blank=True, related_name='archives')
    videos = models.ManyToManyField(Video, blank=True, related_name='archives')


    def __str__(self):
        return f"{self.user}"