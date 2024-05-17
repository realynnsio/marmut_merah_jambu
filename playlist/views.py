from django.shortcuts import render
from .models import Playlist

# Create your views here.
def show_all_playlist(request):
    playlist_all = Playlist.objects.all()

    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A',
        "playlists": playlist_all,
    }
    return render(request, "all_playlist.html", context)

def show_detail_playlist(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }
    return render(request, "detail_playlist.html", context)

def add_playlist_form(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }
    return render(request, "add_playlist_form.html", context)

def add_song_form(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }
    return render(request, "add_song_form.html", context)

def show_detail_song(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }
    return render(request, "detail_song.html", context)

def add_song_to_user_playlist_form(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }
    return render(request, "add_song_to_user_playlist_form.html", context)