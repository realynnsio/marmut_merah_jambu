from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import uuid
from django.http import HttpResponseRedirect
from main.helper.function import *
from cru_registrasi.query import *
from datetime import date, datetime
import datetime
import time


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
        result = row
        print(result)

    context = {'playlists' : result}
    return render(request, "all_playlist.html", context)

def show_detail_playlist(request, id):
    playlist_info = []
    songs = []
    is_own_playlist = False
    email_logged_in = request.session['email']

    query1 = f"""
                SELECT judul, nama, total_durasi, tanggal_dibuat, deskripsi, id_playlist FROM MARMUT.USER_PLAYLIST, MARMUT.AKUN WHERE id_playlist = '{id}' AND email_pembuat = email
            """

    query2 = f"""
                SELECT K.judul, AK.nama, K.id
                FROM MARMUT.PLAYLIST_SONG PS, MARMUT.SONG S, MARMUT.KONTEN K, MARMUT.ARTIST AT, MARMUT.AKUN AK
                WHERE PS.id_playlist = '{id}' AND PS.id_song = S.id_konten AND S.id_konten = K.id AND S.id_artist = AT.id AND AT.email_akun = AK.email
            """

    query3 = f"""
                SELECT email_pembuat FROM MARMUT.USER_PLAYLIST WHERE id_playlist = '{id}'    
            """
    with connection.cursor() as cursor:
        cursor.execute(query1)
        row = cursor.fetchall()
        playlist_info = row

        cursor.execute(query2)
        row = cursor.fetchall()
        songs = row
        print(len(row))

        cursor.execute(query3)
        row = cursor.fetchone()
        is_own_playlist = email_logged_in == row[0]
        
    context = {
        'playlist_info' : playlist_info,
        'own_playlist' : is_own_playlist,
        'songs' : songs,
    }
    return render(request, "detail_playlist.html", context)

@csrf_exempt
def add_playlist_form(request):
    context = {}
    return render(request, "add_playlist_form.html", context)

@csrf_exempt
def add_playlist(request):
    if request.method == 'POST':

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

def edit_playlist_form(request, id):
    context = {
        'id_playlist' : id,
    }
    return render(request, "edit_playlist_form.html", context)

@csrf_exempt
def edit_playlist(request, id):
    if request.method == 'POST':

        judul = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi')

        print(judul)
        print(deskripsi)

        if (not(judul and deskripsi)):
            context = {'pesan': "Harap isi data dengan benar!",
                       'gagal': True}
            return render(request, "add_playlist_form.html", context)
        else:

            query1 = f"""
                        UPDATE MARMUT.USER_PLAYLIST
                        SET judul = '{judul}', deskripsi = '{deskripsi}'
                        WHERE id_playlist = '{id}'
                        """
            
            with connection.cursor() as cursor:
                cursor.execute(query1)
                
            return HttpResponseRedirect(reverse('playlist:show_playlist'))

def add_song_form(request, id):
    all_songs = []
    query1 = f"""
                SELECT K.judul, AK.nama, K.id
                FROM MARMUT.SONG S, MARMUT.KONTEN K, MARMUT.ARTIST AT, MARMUT.AKUN AK
                WHERE S.id_konten = K.id AND S.id_artist = AT.id AND AT.email_akun = AK.email
                """

    with connection.cursor() as cursor:
        cursor.execute(query1)
        row = cursor.fetchall()
        all_songs = row
        
    context = {
        'songs': all_songs,
        'id_playlist' : id,
    }
    return render(request, "add_song_form.html", context)

def delete_song(request, id):

    query1 = f"""
                DELETE FROM MARMUT.PLAYLIST_SONG WHERE id_song = '{id}'
                """

    with connection.cursor() as cursor:
        cursor.execute(query1)

    return HttpResponseRedirect(reverse('playlist:show_playlist'))

def delete_playlist(request, id):
    query1 = f"""
                DELETE FROM MARMUT.USER_PLAYLIST WHERE id_playlist = '{id}'
                """
    query2 = f"""
                DELETE FROM MARMUT.PLAYLIST_SONG WHERE id_playlist = '{id}'
                """
    query3 = f"""
                DELETE FROM MARMUT.PLAYLIST WHERE id = '{id}'
                """

    with connection.cursor() as cursor:
        cursor.execute(query1)
        cursor.execute(query2)
        cursor.execute(query3)

    return HttpResponseRedirect(reverse('playlist:show_playlist'))

def show_detail_song(request, id_song, id_playlist):
    songs_info=[]
    songwriter_info=[]
    query1 = f"""
                SELECT K.judul, G.genre, AK.nama, K.durasi, K.tanggal_rilis, K.tahun, S.total_play, S.total_download, AB.judul
                FROM MARMUT.SONG S, MARMUT.KONTEN K, MARMUT.ARTIST AT, MARMUT.AKUN AK, MARMUT.GENRE G, MARMUT.ALBUM AB
                WHERE S.id_konten = '{id_song}' AND S.id_konten = K.id AND S.id_artist = AT.id AND AT.email_akun = AK.email AND G.id_konten = K.id AND AB.id = S.id_album
                """

    query2 = f"""
                SELECT A.nama
                FROM MARMUT.SONGWRITER SW, MARMUT.SONGWRITER_WRITE_SONG SWS, MARMUT.AKUN A
                WHERE SWS.id_song = '{id_song}' AND SWS.id_songwriter = SW.id AND SW.email_akun = A.email
                """

    with connection.cursor() as cursor:
        cursor.execute(query1)
        row = cursor.fetchall()
        songs_info = row

        cursor.execute(query2)
        row = cursor.fetchall()
        songwriter_info = row

    context = {
        'id_song': id_song,
        'infos' : songs_info,
        'songwriter' : songwriter_info,
        'id_playlist' : id_playlist
    }
    return render(request, "detail_song.html", context)

@csrf_exempt
def add_song_to_user_playlist_form(request, id_playlist):
    id_song = request.POST.get("lagu")

    query1 = f"""
                INSERT INTO MARMUT.PLAYLIST_SONG VALUES ('{id_playlist}', '{id_song}')
                """

    with connection.cursor() as cursor:
        cursor.execute(query1)

    return HttpResponseRedirect(reverse('playlist:show_playlist'))

def add_song_to_playlist_form(request, id_song):
    result = []
    email_logged_in = request.session['email']
    query = f"""
                SELECT * FROM MARMUT.USER_PLAYLIST WHERE email_pembuat = '{email_logged_in}'
            """

    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()
        result = row

    context = {'playlists' : result,
               'id_song' : id_song}
    return render(request, "add_song_to_playlist_form.html", context)

@csrf_exempt
def add_song_to_playlist(request, id_song):
    id_playlist = request.POST.get("playlist")
    
    query1 = f"""
                INSERT INTO MARMUT.PLAYLIST_SONG VALUES ('{id_playlist}', '{id_song}')
                """

    with connection.cursor() as cursor:
        cursor.execute(query1)

    return HttpResponseRedirect(reverse('playlist:show_playlist'))

@csrf_exempt
def play_song(request, id_song):
    email_logged_in = request.session['email']
    curr_timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    query1 = f"""
                INSERT INTO MARMUT.AKUN_PLAY_SONG VALUES ('{email_logged_in}', '{id_song}', '{curr_timestamp}')
                """

    with connection.cursor() as cursor:
        cursor.execute(query1)
        
    print(email_logged_in)
    print(curr_timestamp)
    print(id_song)

    return HttpResponseRedirect(reverse('playlist:show_playlist'))


def show_detail_song_from_podcast(request, id_song):
    songs_info=[]
    songwriter_info=[]
    query1 = f"""
                SELECT K.judul, G.genre, AK.nama, K.durasi, K.tanggal_rilis, K.tahun, S.total_play, S.total_download, AB.judul
                FROM MARMUT.SONG S, MARMUT.KONTEN K, MARMUT.ARTIST AT, MARMUT.AKUN AK, MARMUT.GENRE G, MARMUT.ALBUM AB
                WHERE S.id_konten = '{id_song}' AND S.id_konten = K.id AND S.id_artist = AT.id AND AT.email_akun = AK.email AND G.id_konten = K.id AND AB.id = S.id_album
                """

    query2 = f"""
                SELECT A.nama
                FROM MARMUT.SONGWRITER SW, MARMUT.SONGWRITER_WRITE_SONG SWS, MARMUT.AKUN A
                WHERE SWS.id_song = '{id_song}' AND SWS.id_songwriter = SW.id AND SW.email_akun = A.email
                """

    with connection.cursor() as cursor:
        cursor.execute(query1)
        row = cursor.fetchall()
        songs_info = row

        cursor.execute(query2)
        row = cursor.fetchall()
        songwriter_info = row

    context = {
        'id_song': id_song,
        'infos' : songs_info,
        'songwriter' : songwriter_info,
    }
    return render(request, "detail_song_from_chart.html", context)