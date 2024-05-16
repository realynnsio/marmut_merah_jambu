from django.urls import path
from royalti.views import show_list_royalti

app_name = 'royalti'

urlpatterns = [
    path('', show_list_royalti, name='show_list_royalti'),
]