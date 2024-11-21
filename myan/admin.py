from django.contrib import admin
from .models import Playlist, Song, Album

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'playlist', 'plays')
    search_fields = ('name', 'artist')
    list_filter = ('playlist',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date')
    search_fields = ('name',)

