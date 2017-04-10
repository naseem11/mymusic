from django.db import models
from .file_validator import validate_file_extension
from django.contrib.auth.models import User


# Create your models here.
class Album(models.Model):
    uploader=models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    genre = models.CharField(blank=True, max_length=50)
    artwork = models.ImageField(upload_to='artworks')

    def __str__(self):
        return self.title + ' by ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    duration = models.DecimalField(blank=True, max_digits=4, decimal_places=2)
    file = models.FileField(upload_to='songs', validators=[validate_file_extension])

    def __str__(self):
        return self.title

