from django.urls import path
from crud_kelola_album_song.views import show_list_album

app_name = 'crud_kelola_album_song'

urlpatterns = [
    path('all/', show_list_album, name='show_list_album'),
]