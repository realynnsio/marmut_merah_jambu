from django.shortcuts import render, redirect, reverse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import uuid
from django.http import HttpResponseRedirect
from main.helper.function import *
from cru_registrasi.query import *
from .query import *

# Create your views here.
def show_dashboard(request):
    email = request.session.get('email')

    with connection.cursor() as cursor:
        cursor.execute("set search_path to marmut;")
        if not request.session.get('is_label'):
            cursor.execute(get_user(email))
            res = parse(cursor)
        else:
            cursor.execute(
                f""" SELECT * FROM LABEL WHERE email = '{email}';
                """
            )
            res = parse(cursor)
    
    current_user = res[0]
    gender = ""
    role_string = ""
    playlists = []
    
    if not request.session.get('is_label'):
        if current_user.get('gender') == 0:
            gender = "Perempuan"
        else:
            gender = "Laki-Laki"
        
        if request.session.get('is_artist'):
            role_string += "Artist \n"
        if request.session.get('is_songwriter'):
            role_string += "Songwriter \n"
        if request.session.get('is_podcaster'):
            role_string += "Podcaster \n"
        
        query = f"""
                    SELECT * FROM MARMUT.USER_PLAYLIST WHERE email_pembuat = '{email}'
                """

        with connection.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchall()
            playlists = row
    
    songs = []
    if request.session.get('is_artist') or request.session.get('is_songwriter'):
        cursor = connection.cursor()
        cursor.execute("set search_path to marmut;")
        cursor.execute(get_artist_id(email))

        res = parse(cursor)
        artist_id = '00000000-0000-0000-0000-000000000000'
        if res:
            artist_id = res[0].get('id')

        cursor.execute(get_songwriter_id(email))
        res = parse(cursor)
        songwriter_id = '00000000-0000-0000-0000-000000000000'
        if res:
            songwriter_id = res[0].get('id')

        cursor.execute(get_songs(artist_id, songwriter_id))
        res = cursor.fetchall()
        songs = res
    
    podcasts = []
    if request.session.get('is_podcaster'):
        cursor = connection.cursor()

        query = f"""
        SELECT KONTEN.judul
        FROM MARMUT.PODCAST
        LEFT JOIN MARMUT.KONTEN ON id_konten = id
        WHERE PODCAST.email_podcaster = '{email}';
        """
        cursor.execute(query)
        res = cursor.fetchall()
        podcasts = res
    
    if len(playlists) <= 0:
        has_playlist = False
    else:
        has_playlist = True
    
    label_albums = []
    if request.session.get('is_label'):
        cursor = connection.cursor()

        cursor.execute("set search_path to marmut;")
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
            label_albums.append(item)

    context = {
        "user" : current_user,
        "gender" : gender,
        "roles" : role_string,
        "playlists" : playlists,
        "has_playlist" : has_playlist,
        "songs" : songs,
        "podcasts" : podcasts,
        "label_albums" : label_albums,
    }
    return render(request, "dashboard.html", context)
