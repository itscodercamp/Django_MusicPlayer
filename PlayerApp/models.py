from django.db import models
from django.core.validators import FileExtensionValidator, MaxValueValidator
from django.contrib.auth.models import User

class Album(models.Model):
    album = models.CharField(max_length=125,null=True, blank=True)
    def __str__(self):
        return self.album

class Artist(models.Model):
    artist = models.CharField(max_length=125,null=True, blank=True)
    def __str__(self):
        return self.artist

class Genre(models.Model):
    genre = models.CharField(max_length=125,null=True, blank=True)
    def __str__(self):
        return self.genre


class Music_Uploader(models.Model):
    Song_Title = models.CharField(max_length=125,null=True, blank=True)
    # slug = models.SlugField(unique=True ,null=True, blank=True)
    ablums = models.ForeignKey(Album ,on_delete=models.CASCADE)
    artists = models.ForeignKey(Artist ,on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre ,on_delete=models.CASCADE)
    # duration = models.CharField(max_length=15 ,null=True, blank=True)
    image = models.ImageField(upload_to='Songs/Song_images/',null=True, blank=True)
    audio = models.FileField(
    upload_to='Songs/All_Songs',
    null=True,
    blank=True,
    # validators=[
    #     FileExtensionValidator(allowed_extensions=['mp3', 'wav']),
    #     MaxValueValidator(5 * 1024 * 1024, message="File size must be 5 MB or less."),
    # ],
    help_text="File size must be 5 MB or less"
)

    def __str__(self):
        return  self.Song_Title
    
class PlayLists(models.Model):
    Playlist_Title = models.CharField(max_length=125,null=True,blank=True)
    User_Name = models.ForeignKey(User , on_delete=models.CASCADE ,null=True,blank=True)
    Songs = models.ManyToManyField(Music_Uploader, related_name='playlists' ,null=True,blank=True)

    def __str__(self):
        return  self.Playlist_Title