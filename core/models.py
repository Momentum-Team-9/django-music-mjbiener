from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    release_year = models.IntegerField(blank=True, null=True)
    album_photo = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.artist}, {self.release_year}"


class Track(models.Model):
    name = models.CharField(max_length=250)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="tracks")

    def __str__(self):
        return f"{self.name}, {self.album}"