from django.urls import path
from main.views import show_main, show_login

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('login/', show_login, name='show_login'),
]