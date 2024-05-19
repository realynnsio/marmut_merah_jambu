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
def show_song_list_album(request, album_id):
    email = request.session.get('email')

    songs = []
    judul_album = ""

    with connection.cursor() as cursor:
        cursor.execute("set search_path to marmut;")
        cursor.execute(
            f"""
                SELECT *
                FROM KONTEN JOIN SONG ON SONG.id_konten = KONTEN.id
                WHERE SONG.id_album = '{album_id}'
                ;
            """
        )
        res = parse(cursor)

        for song in res:
            songs.append(song)

        cursor.execute(
            f"""
                SELECT judul
                FROM ALBUM
                WHERE id = '{album_id}';
            """
        )
        judul_album = parse(cursor)[0].get('judul')

    context = {
        "songs" : songs,
        "judul_album" : judul_album,
        "id_album" : album_id,
    }
    return render(request, "daftar_lagu.html", context)

def create_song(request, album_id):
    email = request.session.get('email')
    cursor = connection.cursor()
    cursor.execute("set search_path to marmut;")

    cursor.execute(
        f""" SELECT *
        FROM ALBUM
        WHERE id = '{album_id}';
        """
    )
    album = parse(cursor)[0]

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
        "album" : album,
        "artists" : artists,
        "songwriters" : songwriters,
        "genres" : genres,
        "artist_name" : artist_name,
        "songwriter_name" : songwriter_name,
    }
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
    email = request.session.get('email')

    cursor = connection.cursor()
    cursor.execute("set search_path to marmut;")
    album = []

    cursor.execute(
        f""" SELECT id
        FROM LABEL
        WHERE email = '{email}';
        """
    )
    id_label = parse(cursor)[0].get('id')

    cursor.execute(
        f"""
        SELECT DISTINCT
            a.id,
            a.judul,
            l.nama,
            a.jumlah_lagu,
            a.total_durasi
        FROM
            ALBUM as a
            JOIN LABEL as l ON a.id_label = l.id
        WHERE
            a.id_label = '{id_label}'
        ;
    """
    )
    res = parse(cursor)
    for item in res:
        album.append(item)

    context = {'list_album': album}
    return render(request, "label_list_album.html", context)

def show_label_song_list(request, album_id):
    email = request.session.get('email')

    cursor = connection.cursor()
    cursor.execute("set search_path to marmut;")

    cursor.execute(
        f"""
            SELECT *
            FROM KONTEN JOIN SONG ON SONG.id_konten = KONTEN.id
            WHERE SONG.id_album = '{album_id}'
            ;
        """
    )
    res = parse(cursor)

    songs = []
    for song in res:
        songs.append(song)

    cursor.execute(
        f"""
            SELECT judul
            FROM ALBUM
            WHERE id = '{album_id}';
        """
    )
    judul_album = parse(cursor)[0].get('judul')

    context = {
        "songs" : songs,
        "judul_album" : judul_album,
        "id_album" : album_id,
    }

    return render(request, "label_daftar_lagu.html", context)


def daftar_album(request):
    email = request.session.get('email')

    cursor = connection.cursor()
    cursor.execute("set search_path to marmut;")

    album = []

    if request.session.get('is_artist') and request.session.get('is_songwriter'):
        cursor.execute(get_artist_id(email))
        res = parse(cursor)

        artist_id = res[0].get('id')

        cursor.execute(get_artist_songwriter_albums(artist_id))
        res = parse(cursor)
        for item in res:
            album.append(item)

    elif request.session.get('is_artist'):
        cursor.execute(get_artist_id(email))
        res = parse(cursor)

        artist_id = res[0].get('id')

        cursor.execute(get_artist_albums(artist_id))
        res = parse(cursor)
        for item in res:
            album.append(item)
    
    elif request.session.get('is_songwriter'):
        cursor.execute(get_songwriter_id(email))
        res = parse(cursor)

        songwriter_id = res[0].get('id')

        cursor.execute(get_songwriter_albums(songwriter_id))
        res = parse(cursor)
        for item in res:
            album.append(item)
    
    context = {'list_album': album}
    
    return render(request, 'list_album.html', context)

def add_song_to_album(request):
    if request.method == 'POST':
        staticAlbum = request.POST.get('staticAlbum')
        judul = request.POST.get('judul')
        artist = request.POST.get('artist')
        songwriters = request.POST.getlist('songwriters')
        genres = request.POST.getlist('genres')
        durasi = request.POST.get('durasi')

        cursor = connection.cursor()
        cursor.execute("set search_path to marmut;")

        id_konten = uuid.uuid4()
        query1 = f"""
            INSERT INTO KONTEN VALUES ('{id_konten}', '{judul}', '{datetime.date.today()}', '{datetime.date.today().year}', {durasi});
            """
        cursor.execute(query1)

        cursor.execute(
            f"""
                SELECT id
                FROM ALBUM
                WHERE judul = '{staticAlbum}';
            """
        )
        id_album = parse(cursor)[0].get('id')

        cursor.execute(
            f"""
                SELECT ARTIST.id
                FROM ARTIST JOIN AKUN ON ARTIST.email_akun = AKUN.email
                WHERE AKUN.nama = '{artist}';
            """
        )
        id_artist = parse(cursor)[0].get('id')
        query3 = f"""
            INSERT INTO SONG VALUES ('{id_konten}', '{id_artist}', '{id_album}', 0, 0);
        """
        cursor.execute(query3)

        for songwriter in songwriters:
            cursor.execute(
                f"""
                    SELECT SONGWRITER.id
                    FROM SONGWRITER JOIN AKUN ON SONGWRITER.email_akun = AKUN.email
                    WHERE AKUN.nama = '{songwriter}';
                """
            )
            id_songwriter = parse(cursor)[0].get('id')

            cursor.execute(
                f"""
                    INSERT INTO SONGWRITER_WRITE_SONG VALUES ('{id_songwriter}', '{id_konten}');
                """
            )

        for genre in genres:
            cursor.execute(
                f"""
                    INSERT INTO GENRE VALUES ('{id_konten}', '{genre}');
                """
            )

    return HttpResponseRedirect(reverse('crud_kelola_album_song:show_song_list_album', kwargs={'album_id': id_album}))

def add_album(request):
    if request.method == 'POST':
        judul = request.POST.get('judul')
        label = request.POST.get('label')
        judu_lagu_pertama = request.POST.get('judul_lagu_pertama')
        artist = request.POST.get('artist')
        songwriters = request.POST.getlist('songwriters')
        genres = request.POST.getlist('genres')
        durasi = request.POST.get('durasi')

        cursor = connection.cursor()
        cursor.execute("set search_path to marmut;")

        id_konten = uuid.uuid4()
        query1 = f"""
            INSERT INTO KONTEN VALUES ('{id_konten}', '{judu_lagu_pertama}', '{datetime.date.today()}', '{datetime.date.today().year}', {durasi});
            """
        cursor.execute(query1)

        id_album = uuid.uuid4()
        cursor.execute(
            f"""
                SELECT id
                FROM LABEL
                WHERE nama = '{label}';
            """
        )
        id_label = parse(cursor)[0].get('id')
        query2 = f"""
            INSERT INTO ALBUM VALUES ('{id_album}', '{judul}', 0, '{id_label}', 0);
        """
        cursor.execute(query2)


        cursor.execute(
            f"""
                SELECT ARTIST.id
                FROM ARTIST JOIN AKUN ON ARTIST.email_akun = AKUN.email
                WHERE AKUN.nama = '{artist}';
            """
        )
        id_artist = parse(cursor)[0].get('id')
        query3 = f"""
            INSERT INTO SONG VALUES ('{id_konten}', '{id_artist}', '{id_album}', 0, 0);
        """
        cursor.execute(query3)

        for songwriter in songwriters:
            cursor.execute(
                f"""
                    SELECT SONGWRITER.id
                    FROM SONGWRITER JOIN AKUN ON SONGWRITER.email_akun = AKUN.email
                    WHERE AKUN.nama = '{songwriter}';
                """
            )
            id_songwriter = parse(cursor)[0].get('id')

            cursor.execute(
                f"""
                    INSERT INTO SONGWRITER_WRITE_SONG VALUES ('{id_songwriter}', '{id_konten}');
                """
            )

        for genre in genres:
            cursor.execute(
                f"""
                    INSERT INTO GENRE VALUES ('{id_konten}', '{genre}');
                """
            )

    return HttpResponseRedirect(reverse('crud_kelola_album_song:daftar_album'))

def delete_album(request, album_id):
    cursor = connection.cursor()
    cursor.execute("set search_path to marmut;")

    cursor.execute(
        f"""
            DELETE FROM ALBUM
            WHERE id = '{album_id}';
        """
    )

    return HttpResponseRedirect(reverse('crud_kelola_album_song:daftar_album'))

def delete_song_from_album(request, song_id):
    cursor = connection.cursor()
    cursor.execute("set search_path to marmut;")

    cursor.execute(
        f"""
            SELECT id_album
            FROM SONG
            WHERE id_konten = '{song_id}';
        """
    )
    id_album = parse(cursor)[0].get('id_album')

    cursor.execute(
        f"""
            DELETE FROM SONG
            WHERE id_konten = '{song_id}';
        """
    )

    cursor.execute(
        f"""
            DELETE FROM KONTEN
            WHERE id = '{song_id}';
        """
    )

    return HttpResponseRedirect(reverse('crud_kelola_album_song:daftar_album'))

def delete_album_label(request, album_id):
    cursor = connection.cursor()
    cursor.execute("set search_path to marmut;")

    cursor.execute(
        f"""
            DELETE FROM ALBUM
            WHERE id = '{album_id}';
        """
    )

    return HttpResponseRedirect(reverse('crud_kelola_album_song:show_label_album'))

def delete_song_label(request, song_id):
    cursor = connection.cursor()
    cursor.execute("set search_path to marmut;")

    cursor.execute(
        f"""
            SELECT id_album
            FROM SONG
            WHERE id_konten = '{song_id}';
        """
    )
    id_album = parse(cursor)[0].get('id_album')

    cursor.execute(
        f"""
            DELETE FROM SONG
            WHERE id_konten = '{song_id}';
        """
    )

    cursor.execute(
        f"""
            DELETE FROM KONTEN
            WHERE id = '{song_id}';
        """
    )

    return HttpResponseRedirect(reverse('crud_kelola_album_song:show_label_album'))

def show_detail_song(request, song_id):
    songs_info=[]
    songwriter_info=[]
    query1 = f"""
                SELECT K.judul, G.genre, AK.nama, K.durasi, K.tanggal_rilis, K.tahun, S.total_play, S.total_download, AB.judul
                FROM MARMUT.SONG S, MARMUT.KONTEN K, MARMUT.ARTIST AT, MARMUT.AKUN AK, MARMUT.GENRE G, MARMUT.ALBUM AB
                WHERE S.id_konten = '{song_id}' AND S.id_konten = K.id AND S.id_artist = AT.id AND AT.email_akun = AK.email AND G.id_konten = K.id AND AB.id = S.id_album
                """

    query2 = f"""
                SELECT A.nama
                FROM MARMUT.SONGWRITER SW, MARMUT.SONGWRITER_WRITE_SONG SWS, MARMUT.AKUN A
                WHERE SWS.id_song = '{song_id}' AND SWS.id_songwriter = SW.id AND SW.email_akun = A.email
                """

    with connection.cursor() as cursor:
        cursor.execute(query1)
        row = cursor.fetchall()
        songs_info = row

        cursor.execute(query2)
        row = cursor.fetchall()
        songwriter_info = row

    context = {
        'id_song': song_id,
        'infos' : songs_info,
        'songwriter' : songwriter_info,
    }
    return render(request, "detail_song_album.html", context)