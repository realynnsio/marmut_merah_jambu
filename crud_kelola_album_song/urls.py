from django.urls import path
from crud_kelola_album_song.views import show_song_list_album, daftar_album, show_detail_song
from crud_kelola_album_song.views import create_song, create_album, delete_album
from crud_kelola_album_song.views import show_label_album, show_label_song_list, add_album, delete_song_from_album
from crud_kelola_album_song.views import add_song_to_album, delete_album_label, delete_song_label


app_name = 'crud_kelola_album_song'

urlpatterns = [
    path('', daftar_album, name='daftar_album'),
    path('detail/<str:album_id>/', show_song_list_album, name='show_song_list_album'),
    path('add-song/<str:album_id>/', create_song, name='create_song'),
    path('add/', create_album, name='create_album'),
    path('label/', show_label_album, name='show_label_album'),
    path('label/detail/<str:album_id>/', show_label_song_list, name='show_label_song_list'),
    path('label/delete/<str:album_id>/', delete_album_label, name='delete_album_label'),
    path('label/delete-song/<str:song_id>/', delete_song_label, name='delete_song_label'),
    path('add-album/', add_album, name='add_album'),
    path('delete/<str:album_id>/', delete_album, name='delete_album'),
    path('delete-song/<str:song_id>/', delete_song_from_album, name='delete_song_from_album'),
    path('detail-song/<str:song_id>/', show_detail_song, name="show_detail_song"),
    path('add-song-to-album/', add_song_to_album, name='add_song_to_album'),
]