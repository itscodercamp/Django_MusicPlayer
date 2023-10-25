from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
from django.http import JsonResponse
from django.shortcuts import redirect, render ,get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth import login ,authenticate
from .models import *
from django.shortcuts import HttpResponse


def index(request):
    username = request.user
    All_Music = Music_Uploader.objects.all()

    if username.is_authenticated:
        playlists = PlayLists.objects.filter(User_Name=username)
    else:
        playlists = None

    context = {
        'user': username,
        'Songs': All_Music,
        'playlists': playlists,
    }
    return render(request, 'MusicPlayer/Layout.html', context)

def logout_views(request):
    logout(request)
    return redirect('home')


@login_required
def create_playlist(request):
    if request.method == 'POST':
        playlist_title = request.POST.get('playlist_title')
        user = request.user  # Get the logged-in user
        new_playlist = PlayLists(Playlist_Title=playlist_title, User_Name=user)
        new_playlist.save()
        return redirect('create_playlist')  # Redirect to the same page or another as needed
    else:
        playlists = PlayLists.objects.filter(User_Name=request.user)  # Filter playlists for the logged-in user
        return render(request, 'create_playlist.html', {'playlists': playlists})

def add_songs_to_playlist(request, playlist_id):
    playlist = PlayLists.objects.get(id=playlist_id)
    songs = Music_Uploader.objects.all()
    playlists = PlayLists.objects.filter(User_Name=request.user)  # Filter playlists for the logged-in user
    user = request.user

    if request.method == 'POST':
        song_id = request.POST.get('song_id')
        song = Music_Uploader.objects.get(id=song_id)
        playlist.Songs.add(song)
        playlist.save()

    return render(request, 'add_songs_to_playlist.html', {'playlist': playlist, 'songs': songs ,'playlists': playlists,'username': user})


def delete_playlist(request, playlist_id):
    if request.method == 'POST':
        playlist = PlayLists.objects.get(id=playlist_id)
        playlist.delete()
    return redirect('create_playlist')

from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password)
        user.email = email
        user.save()
        login(request, user)
        return redirect('profile')
    return render(request, 'registration/register.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})