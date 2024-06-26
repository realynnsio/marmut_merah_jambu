"""
URL configuration for marmut_merah_jambu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('dashboard', include('dashboard.urls')),
    path('playlist/', include('playlist.urls')),
    path('cru_registrasi/', include('cru_registrasi.urls')),
    path('albums/', include('crud_kelola_album_song.urls')),
    path('podcast/', include('kelola_podcast.urls')),
    path('chart/', include('chart.urls')),
    path('royalti/', include('royalti.urls')),
    path('langganan_paket/', include('langganan_paket.urls')),
    path('pencarian/', include('pencarian.urls')),
    path('downloaded_songs/', include('downloaded_songs.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)