from django.shortcuts import render, redirect, reverse
import datetime
import re
import uuid
# from event.forms import *
from django.shortcuts import render, redirect
from django.db import InternalError, IntegrityError, connection
from crud_kelola_album_song.query import *
from main.helper.function import parse
# from event.helper import convert_to_slug, convert_to_title
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

# Create your views here.
def show_list_album(request):
    context = {}
    return render(request, "list_album.html", context)

def show_song_list_album(request):
    context = {}
    return render(request, "daftar_lagu.html", context)

def create_song(request):
    context = {}
    return render(request, "create_lagu.html", context)

def create_album(request):
    email = request.session.get('email')
    cursor = connection.cursor()
    cursor.execute("set search_path to marmut;")

    cursor.execute("SELECT nama FROM LABEL;")
    res = parse(cursor)

    labels = []
    for label in res:
        labels.append(label)

    cursor.execute("SELECT akun.nama FROM AKUN JOIN ARTIST ON akun.email = artist.email_akun;")
    res = parse(cursor)

    artists = []
    for artist in res:
        artists.append(artist)


    cursor.execute("SELECT akun.nama FROM AKUN JOIN SONGWRITER ON akun.email = songwriter.email_akun;")
    res = parse(cursor)

    songwriters = []
    for songwriter in res:
        songwriters.append(songwriter)

    cursor.execute("SELECT DISTINCT genre FROM GENRE;")
    res = parse(cursor)

    genres = []
    for genre in res:
        genres.append(genre)
    
    artist_name = ""
    songwriter_name = ""

    if request.session.get('is_artist'):
        cursor.execute(get_artist_nama(email))
        res = parse(cursor)
        artist_name = res[0].get('nama')
    
    if request.session.get('is_songwriter'):
        cursor.execute(get_songwriter_nama(email))
        res = parse(cursor)
        songwriter_name = res[0].get('nama')

    context = {
        "labels" : labels,
        "artists" : artists,
        "songwriters" : songwriters,
        "genres" : genres,
        "artist_name" : artist_name,
        "songwriter_name" : songwriter_name,
    }
    return render(request, "create_album.html", context)


def show_label_album(request):
    context = {}
    return render(request, "label_list_album.html", context)

def show_label_song_list(request):
    context = {}
    return render(request, "label_daftar_lagu.html", context)


def daftar_album(request):
    email = request.session.get('email')

    cursor = connection.cursor()
    cursor.execute("set search_path to marmut;")

    album = []

    if request.session.get('is_artist'):
        cursor.execute(get_artist_id(email))
        res = parse(cursor)

        artist_id = res[0].get('id')

        cursor.execute(get_artist_albums(artist_id))
        res = parse(cursor)
        for item in res:
            album.append(item)
    
    if request.session.get('is_songwriter'):
        cursor.execute(get_songwriter_id(email))
        res = parse(cursor)

        songwriter_id = res[0].get('id')

        cursor.execute(get_songwriter_albums(songwriter_id))
        res = parse(cursor)
        for item in res:
            album.append(item)
    
    context = {'list_album': album}
    
    return render(request, 'list_album.html', context)

def add_album(request):
    if request.method == 'POST':
        judul = request.POST.get('judul')
        label = request.POST.get('label')
        judu_lagu_pertama = request.POST.get('judul_lagu_pertama')
        artist = request.POST.get('artist')
        songwriters = request.POST.getlist('songwriters')
        genres = request.POST.getlist('genres')
        durasi = request.POST.get('durasi')

        


    return HttpResponseRedirect(reverse('crud_kelola_album_song:daftar_album'))