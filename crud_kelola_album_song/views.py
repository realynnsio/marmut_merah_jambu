from django.shortcuts import render
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
    context = {}
    return render(request, "create_album.html", context)

def show_label_album(request):
    context = {}
    return render(request, "label_list_album.html", context)

def show_label_song_list(request):
    context = {}
    return render(request, "label_daftar_lagu.html", context)


def daftar_album(request):
    cursor = connection.cursor()
    cursor.execute("set search_path to marmut;")
    query = get_album_query()
    cursor.execute(query)
    res = parse(cursor)
    album = []
    for item in res:
        album.append(item)
    context = {'list_album': album}
    
    return render(request, 'list_album.html', context)
