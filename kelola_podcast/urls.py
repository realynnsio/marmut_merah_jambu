from django.urls import path
from kelola_podcast.views import show_list_podcast, show_list_episode, show_podcast_detail

app_name = 'kelola_podcast'

urlpatterns = [
    path('', show_list_podcast, name='show_list_podcast'),
    path('podcast-details/', show_podcast_detail, name='show_podcast_detail'),
    path('list-episode/', show_list_episode, name='show_list_episode'),
]