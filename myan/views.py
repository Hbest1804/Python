from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Playlist, Song
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Playlist

def home(request):
    # Lấy danh sách playlist (giới hạn 6 mục)
    playlists = Playlist.objects.all()[:6]
    
    # Kiểm tra nếu trường 'plays' không tồn tại trong model Song
    # Đổi truy vấn order_by theo trường hợp lệ, ví dụ: 'id'
    songs = Song.objects.all().order_by('-id')[:10]
    
    return render(request, 'myan/home.html', {
        'playlists': playlists,
        'songs': songs
    })

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            return render(request, 'myan/register.html', {'error': 'Passwords do not match'})
            
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('home')
        except:
            return render(request, 'myan/register.html', {'error': 'Username already exists'})
            
    return render(request, 'myan/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'myan/login.html', {'error': 'Invalid credentials'})
            
    return render(request, 'myan/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def search(request):
    query = request.GET.get('query', '')
    if query:
        # Đảm bảo trường 'artist' và 'album' tồn tại trước khi truy vấn
        results = Song.objects.filter(
            Q(name__icontains=query) |
            Q(artist__icontains=query)  # Đổi nếu 'artist' không phải chuỗi
        )
    else:
        results = []
    return render(request, 'myan/search.html', {'results': results})

from django.shortcuts import render, get_object_or_404
from .models import Playlist

def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    songs = playlist.songs.all()  # Sử dụng related_name đã khai báo
    return render(request, 'myan/playlist_detail.html', {'playlist': playlist, 'songs': songs})

def profile_view(request):
    # Giả sử người dùng đã đăng nhập, lấy thông tin người dùng từ request.user
    user = request.user
    return render(request, 'myan/profile.html', {'user': user})
