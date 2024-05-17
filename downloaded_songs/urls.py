from django.urls import path
from downloaded_songs.views import download_list, delete_song
app_name = 'downloaded_songs'

urlpatterns = [
    path('download/', download_list, name='download_list'),
    path('hapus_song/', delete_song, name='download_list'),
]