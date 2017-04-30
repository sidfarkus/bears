from django.db import models
from django.contrib.auth.models import User

class Collection(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)

class Song(models.Model):
    collection = models.ForeignKey(Collection)
    title = models.TextField()
    album = models.TextField()
    artist = models.TextField()
    composer = models.TextField()
    duration = models.IntegerField()

