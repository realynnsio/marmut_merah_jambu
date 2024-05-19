from django.urls import path
from playlist.views import show_all_playlist, show_detail_playlist, add_playlist_form, add_song_form, show_detail_song, add_song_to_user_playlist_form, add_playlist, delete_song, delete_playlist, edit_playlist, edit_playlist_form, add_song_to_playlist_form, add_song_to_playlist, play_song

app_name = 'playlist'

urlpatterns = [
    path('all/', show_all_playlist, name='show_playlist'),
    path('all/detail-playlist/<str:id>/', show_detail_playlist, name='show_detail_playlist'),
    path('add-playlist-form/', add_playlist_form, name='add_playlist_form'),
    path('add-playlist/', add_playlist, name='add_playlist'),
    path('all/delete-playlist/<str:id>/', delete_playlist, name='delete_playlist'),
    path('edit-playlist/<str:id>/', edit_playlist, name='edit_playlist'),
    path('edit-playlist-form/<str:id>/', edit_playlist_form, name='edit_playlist_form'),
    path('add-song/<str:id>/', add_song_form, name='add_song_form'),
    path('delete-song/<str:id>/', delete_song, name='delete_song'),
    path('detail-song/<str:id_song>/<str:id_playlist>/', show_detail_song, name='detail_song'),
    path('add-song-to-user-playlist/<str:id_playlist>/', add_song_to_user_playlist_form, name='add_song_to_user_playlist_form'),
    path('add-song-to-playlist-form/<str:id_song>/', add_song_to_playlist_form, name='add_song_to_playlist_form'),
    path('add-song-to-playlist/<str:id_song>/', add_song_to_playlist, name='add_song_to_playlist'),
    path('play-song/<str:id_song>/', play_song, name='play_song')
]