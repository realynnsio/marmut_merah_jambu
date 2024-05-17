from django.shortcuts import render, redirect, reverse
from utils.query import execute_raw_query
import uuid
import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db import connection
from .decorators import podcaster_required


@podcaster_required
def show_list_podcast(request):
    user_email = request.session.get('email')

    query = f"""
    SELECT KONTEN.judul, COALESCE(COUNT(id_episode), 0) AS episode, KONTEN.id,
    CASE
        WHEN SUM(EPISODE.durasi) % 60 = 0 THEN (SUM(EPISODE.durasi) / 60) || ' jam'
        WHEN SUM(EPISODE.durasi) / 60 = 0 THEN (SUM(EPISODE.durasi) % 60) || ' menit'
        ELSE (SUM(EPISODE.durasi) / 60) || ' jam ' || (SUM(EPISODE.durasi) % 60) || ' menit'
    END AS total_durasi
    FROM MARMUT.PODCAST
    LEFT JOIN MARMUT.KONTEN ON id_konten = id
    LEFT JOIN MARMUT.EPISODE ON id_konten_podcast = id_konten 
    WHERE PODCAST.email_podcaster = '{user_email}'
    GROUP BY KONTEN.judul, KONTEN.id
    """
    results = execute_raw_query(query)

    result_data = []

    for result in results:
        judul = result[0]
        jumlah_episode = result[1]
        id_konten  = result[2]
        total_durasi = result[3]

        result_data.append({
            'id' : id_konten,
            'judul': judul,
            'jumlah_episode': jumlah_episode,
            'total_durasi' : total_durasi
        })

    context = {'results': result_data}
    return render(request, "list_podcast.html", context)


@podcaster_required
def show_list_episode(request, id_input):
    query = f"""
    SELECT KONTEN.id, EPISODE.id_episode, EPISODE.judul, EPISODE.deskripsi, EPISODE.tanggal_rilis, 
    CASE
        WHEN EPISODE.durasi % 60 = 0 THEN (EPISODE.durasi / 60) || ' jam'
        WHEN EPISODE.durasi / 60 = 0 THEN (EPISODE.durasi % 60) || ' menit'
        ELSE EPISODE.durasi / 60 || ' jam ' || (EPISODE.durasi % 60) || ' menit'
    END AS total_durasi
    FROM MARMUT.KONTEN, MARMUT.PODCAST, MARMUT.EPISODE 
    WHERE id_konten = id AND id_konten_podcast = id_konten AND id = '{id_input}';
    """

    results = execute_raw_query(query)

    result_data = []

    for result in results:
        id_konten = result[0]
        id_episode = result[1]
        judul = result[2]
        deskripsi = result[3]
        durasi = result[4]
        tanggal_rilis = result[5]

        result_data.append({
            'judul': judul,
            'deskripsi': deskripsi,
            'durasi': durasi,
            'tanggal_rilis' : tanggal_rilis,
            'id_konten' : id_konten,
            'id_episode': id_episode
        })
    
    context = {'results': result_data}
    return render(request, 'list_episode.html', context)

def show_podcast_detail(request, id_input):
    query = f"""  
    SELECT KONTEN.judul, AKUN.nama, KONTEN.tanggal_rilis, KONTEN.tahun, EPISODE.judul, EPISODE.deskripsi, EPISODE.tanggal_rilis, string_agg(GENRE.genre, ', ') AS genre,
    CASE
        WHEN EPISODE.durasi % 60 = 0 THEN (EPISODE.durasi / 60) || ' jam'
        WHEN EPISODE.durasi / 60 = 0 THEN (EPISODE.durasi % 60) || ' menit'
        ELSE EPISODE.durasi / 60 || ' jam ' || (EPISODE.durasi % 60) || ' menit'
    END AS total_durasi_episode
    FROM MARMUT.KONTEN LEFT JOIN MARMUT.PODCAST ON PODCAST.id_konten = KONTEN.id 
    LEFT JOIN MARMUT.PODCASTER ON PODCASTER.email = PODCAST.email_podcaster 
    LEFT JOIN MARMUT.AKUN ON AKUN.email = PODCASTER.email 
    LEFT JOIN MARMUT.GENRE ON GENRE.id_konten = KONTEN.id 
    LEFT JOIN MARMUT.EPISODE ON EPISODE.id_konten_podcast = PODCAST.id_konten
    WHERE 
        KONTEN.id = '{id_input}'
    GROUP BY 
        KONTEN.judul, 
        AKUN.nama, 
        KONTEN.tanggal_rilis, 
        KONTEN.tahun, 
        EPISODE.judul, 
        EPISODE.deskripsi, 
        EPISODE.tanggal_rilis, 
        EPISODE.durasi
    """

    query2 = f"""
    SELECT KONTEN.judul,
    CASE
        WHEN SUM(EPISODE.durasi) % 60 = 0 THEN (SUM(EPISODE.durasi) / 60) || ' jam'
        WHEN SUM(EPISODE.durasi) / 60 = 0 THEN (SUM(EPISODE.durasi) % 60) || ' menit'
        ELSE (SUM(EPISODE.durasi) / 60) || ' jam ' || (SUM(EPISODE.durasi) % 60) || ' menit'
    END AS total_durasi
    FROM MARMUT.PODCAST
    LEFT JOIN MARMUT.KONTEN ON id_konten = id
    LEFT JOIN MARMUT.EPISODE ON id_konten_podcast = id_konten 
    WHERE KONTEN.id = '{id_input}'
    GROUP BY KONTEN.judul
    """

    results = execute_raw_query(query)
    results2 = execute_raw_query(query2)

    result_data = []

    result2 = results2[0]
    total_durasi_podcast = result2[1]

    for result in results:
        judul_podcast = result[0]
        nama_podcaster = result[1]
        tanggal_rilis_podcast = result[2]
        tahun_rilis_podcast = result[3]
        judul_episode = result[4]
        deskripsi_episode = result[5]
        tanggal_rilis_episode = result[6]
        genre_podcast = result[7]
        total_durasi_episode = result [8]

        if len(result_data) == 0:
            result_data.append({
                'judul_podcast': judul_podcast,
                'nama_podcaster': nama_podcaster,
                'tanggal_rilis_podcast': tanggal_rilis_podcast,
                'tahun_rilis_podcast' : tahun_rilis_podcast,
                'judul_episode' : judul_episode,
                'deskripsi_episode': deskripsi_episode,
                'tanggal_rilis_episode' : tanggal_rilis_episode,
                'genre_podcast' : genre_podcast,
                'total_durasi_episode' : total_durasi_episode,
                'total_durasi_podcast' : total_durasi_podcast

            })
        else:
            result_data.append({
                'judul_episode' : judul_episode,
                'deskripsi_episode': deskripsi_episode,
                'tanggal_rilis_episode' : tanggal_rilis_episode,
                'genre_podcast' : genre_podcast,
                'total_durasi_episode' : total_durasi_episode,
            })

    context = {'results': result_data}
    return render(request, "podcast_detail.html", context)

@podcaster_required
def show_form_episode(request, id_podcast):


    context = {'data' : id_podcast }
    return render(request, "create_episode.html", context)

@podcaster_required
def show_form_podcast(request):
    context = {}
    return render(request, "create_podcast.html", context)

def add_podcast_raw(judul, genres, konten_id, tanggal_rilis, user_email):

    query1 = f"""
    SELECT AKUN.nama FROM MARMUT.AKUN, MARMUT.PODCASTER WHERE PODCASTER.email = AKUN.email AND PODCASTER.email = '{user_email}'
    """

    results = execute_raw_query(query1)

    result_data = []

    for result in results:
        nama = result[0];

    result_data.append({
        'nama': nama
    })

    query = f"""
    INSERT INTO MARMUT.KONTEN VALUES ('{konten_id}', '{judul}', '{tanggal_rilis}', '{tanggal_rilis.year}', 540)
    """

    with connection.cursor() as cursor:
        cursor.execute(query)

    for genre in genres:
        query1 = f"""
        INSERT INTO MARMUT.GENRE VALUES ('{konten_id}', '{genre}')
        """

        with connection.cursor() as cursor:
            cursor.execute(query1)

    query2 = f"""
    INSERT INTO MARMUT.PODCAST VALUES('{konten_id}', '{user_email}')
    """

    with connection.cursor() as cursor:
            cursor.execute(query2)

def add_episode_raw(id_episode, id_konten_podcast, judul, deskripsi, durasi, tanggal_rilis):

    query = f"""
    INSERT INTO MARMUT.EPISODE  VALUES ('{id_episode}', '{id_konten_podcast}', '{judul}', '{deskripsi}', '{durasi}', '{tanggal_rilis}')
    """

    with connection.cursor() as cursor:
        cursor.execute(query)

def add_podcast(request):
    if request.method == 'POST':
        judul = request.POST.get('judul')
        genres = request.POST.getlist('genre')
        konten_id = uuid.uuid4()
        tanggal_rilis = datetime.date.today();

        user_email = request.session.get('email')

        add_podcast_raw(judul, genres, konten_id, tanggal_rilis, user_email)
        return HttpResponseRedirect(reverse('kelola_podcast:show_list_podcast'))

@podcaster_required
def add_episode(request, id_podcast):
        judul = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi')
        durasi = request.POST.get('durasi')
        episode_id = uuid.uuid4()
        tanggal_rilis = datetime.date.today();

        add_episode_raw(episode_id, id_podcast, judul, deskripsi, durasi, tanggal_rilis)
        return HttpResponseRedirect(reverse('kelola_podcast:show_list_podcast'))
     
@podcaster_required
def delete_episode(request, id_episode, id_konten):
    query = f"""
    DELETE FROM MARMUT.EPISODE WHERE id_episode = '{id_episode}'
    """ 

    with connection.cursor() as cursor:
        cursor.execute(query)

    return HttpResponseRedirect(reverse('kelola_podcast:show_list_episode', kwargs={'id_input': id_konten}))

@podcaster_required
def delete_podcast(request, id_konten):

    query = f"""
    DELETE FROM MARMUT.KONTEN WHERE id = '{id_konten}'
    """

    with connection.cursor() as cursor:
        cursor.execute(query)

    query2 = f"""
    DELETE FROM MARMUT.PODCAST WHERE id_konten = '{id_konten}'
    """

    with connection.cursor() as cursor:
        cursor.execute(query2)
    
    return HttpResponseRedirect(reverse('kelola_podcast:show_list_podcast'))



# def get_email_user(user_email):
#     query = f"""
#     SELECT email FROM AKUN WHERE email = '{user_email}'
#     """

#     return execute_raw_query(query)


