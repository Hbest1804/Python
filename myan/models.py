# models.p
from django.db import models
from django.utils import timezone

# Mô hình Playlist
class Playlist(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Đảm bảo không trùng tên playlist
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='playlist_images/', default='static/images/default-playlist.png')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


# Mô hình Song
class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='songs/', default='songs/default.mp3')
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='songs')
    plays = models.IntegerField(default=0)  # Số lần phát

    def __str__(self):
        return f"{self.name} - {self.artist}"

    # Tăng số lần phát khi bài hát được phát
    def play(self):
        self.plays += 1
        self.save()


# Mô hình Album
class Album(models.Model):
    name = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='album_images/', default='static/images/default-song.png')
    release_date = models.DateField()
    songs = models.ManyToManyField(Song, related_name='albums')  # Một album có nhiều bài hát

    def __str__(self):
        return self.name


