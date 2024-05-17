from django.urls import path
from kelola_podcast.views import show_list_podcast, show_list_episode, show_podcast_detail, show_form_episode, show_form_podcast, delete_episode, delete_podcast, add_episode, add_podcast

app_name = 'kelola_podcast'

urlpatterns = [
    path('', show_list_podcast, name='show_list_podcast'),
    path('podcast-details/<uuid:id_input>', show_podcast_detail, name='show_podcast_detail'),
    path('list-episode/<uuid:id_input>', show_list_episode, name='show_list_episode'),
    path('create-episode/<uuid:id_podcast>', show_form_episode, name='show_form_episode'),
    path('create-podcast', show_form_podcast, name='show_form_podcast'),
    path('delete-episode/<uuid:id_episode>/<uuid:id_konten>', delete_episode, name='delete_episode'),
    path('delete-podcast/<uuid:id_konten>', delete_podcast, name='delete_podcast'),
    path('add-episode/<uuid:id_podcast>', add_episode, name='add_episode'),
    path('add-podcast', add_podcast, name='add_podcast')
]