from django.urls import path
from pencarian.views import search_data,show_search, ke_halaman

app_name = 'pencarian'

urlpatterns = [
    path('search-data/', search_data, name='search_data'),
    path('result/', show_search, name='show_search'),
    path('ke_halaman/', ke_halaman, name='ke_halaman')
]