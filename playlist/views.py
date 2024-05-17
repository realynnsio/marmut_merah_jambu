from django.shortcuts import render, redirect, reverse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import uuid
from django.http import HttpResponseRedirect
from main.helper.function import *
from cru_registrasi.query import *
from datetime import date


# Create your views here.
def show_all_playlist(request):
    result = []
    email_logged_in = request.session['email']
    query = f"""
                SELECT * FROM MARMUT.USER_PLAYLIST WHERE email_pembuat = '{email_logged_in}'
            """

    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()
        print(row)
        result = row
        print(result)

    context = {'playlists' : result}
    return render(request, "all_playlist.html", context)

def show_detail_playlist(request, id):
    playlist_info = []
    query1 = f"""
                SELECT judul, nama, total_durasi, tanggal_dibuat, deskripsi FROM MARMUT.USER_PLAYLIST, MARMUT.AKUN WHERE id_playlist = '{id}' AND email_pembuat = email
            """

    query2 = f"""
                SELECT judul, nama FROM MARMUT.PLAYLIST_SONG,  WHERE id_playlist = '{id}'
            """
    with connection.cursor() as cursor:
        cursor.execute(query1)
        row = cursor.fetchall()
        playlist_info = row
        
    context = {
        'playlist_info' : playlist_info
    }
    return render(request, "detail_playlist.html", context)

@csrf_exempt
def add_playlist_form(request):
    context = {}
    return render(request, "add_playlist_form.html", context)

@csrf_exempt
def add_playlist(request):
    if request.method == 'POST':
        print("JAMAL")
        judul = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi')

        if (not(judul and deskripsi)):
            context = {'pesan': "Harap isi data dengan benar!",
                        'gagal': True}
            return render(request, "add_playlist_form.html", context)
        else:
            email_pembuat = request.session['email']
            id_user_playlist = uuid.uuid4()
            id_playlist = uuid.uuid4()
            tanggal_dibuat = date.today()
            
            query1 = f"""
                        INSERT INTO MARMUT.PLAYLIST VALUES ('{id_playlist}')
                        """
            query2 = f"""
                        INSERT INTO MARMUT.USER_PLAYLIST VALUES ('{email_pembuat}', '{id_user_playlist}', '{judul}', '{deskripsi}', '0', '{tanggal_dibuat}' ,'{id_playlist}', '0')
                        """
            with connection.cursor() as cursor:
                cursor.execute(query1)
                cursor.execute(query2)
            return HttpResponseRedirect(reverse('playlist:show_playlist'))


def add_song_form(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }
    return render(request, "add_song_form.html", context)

def show_detail_song(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }
    return render(request, "detail_song.html", context)

def add_song_to_user_playlist_form(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }
    return render(request, "add_song_to_user_playlist_form.html", context)