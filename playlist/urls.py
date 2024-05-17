from django.urls import path
from playlist.views import show_all_playlist, show_detail_playlist, add_playlist_form, add_song_form, show_detail_song, add_song_to_user_playlist_form, add_playlist

app_name = 'playlist'

urlpatterns = [
    path('all/', show_all_playlist, name='show_playlist'),
    path('all/detail-playlist/<str:id>/', show_detail_playlist, name='show_detail_playlist'),
    path('add-playlist-form/', add_playlist_form, name='add_playlist_form'),
    path('add-playlist/', add_playlist, name='add_playlist'),
    path('add-song/', add_song_form, name='add_song_form'),
    path('detail-song/', show_detail_song, name='detail_song'),
    path('add-song-to-user-playlist/', add_song_to_user_playlist_form, name='add_song_to_user_playlist_form'),
]