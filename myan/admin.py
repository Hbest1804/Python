from django.contrib import admin
from .models import Song, Playlist

# Tạo SongInline để hiển thị các bài hát trong Playlist
class SongInline(admin.TabularInline):
    model = Song
    extra = 1  # Số dòng mặc định để thêm bài hát mới vào playlist

class PlaylistAdmin(admin.ModelAdmin):
    inlines = [SongInline]
    list_display = ('name', 'cover_image', 'get_song_count')  # Hiển thị tên playlist, ảnh bìa và số bài hát
    search_fields = ['name']  # Tìm kiếm playlist theo tên

    def get_song_count(self, obj):
        return obj.song_set.count()  # Đếm số bài hát trong playlist (sử dụng song_set cho ForeignKey)
    get_song_count.short_description = 'Number of Songs'  # Đổi tên cột

# Đăng ký các mô hình và các tùy chỉnh admin
admin.site.register(Song)
admin.site.register(Playlist, PlaylistAdmin)


