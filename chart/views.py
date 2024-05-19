from django.shortcuts import render
from utils.query import execute_raw_query


def show_chart(request):
    context = {}
    return render(request, "list_chart.html", context)

def chart_detail_daily(request):
    query = """
    SELECT DISTINCT SONG.id_konten, KONTEN.judul, KONTEN.tanggal_rilis, AKUN.nama, COALESCE(COUNT(AKUN_PLAY_SONG.waktu),0 ) AS total_plays
    FROM MARMUT.KONTEN, MARMUT.SONG, MARMUT.AKUN_PLAY_SONG, MARMUT.AKUN, MARMUT.ARTIST 
    WHERE AKUN_PLAY_SONG.waktu >= CURRENT_DATE - INTERVAL '1 days' 
    AND SONG.id_konten = AKUN_PLAY_SONG.id_song 
    AND SONG.id_konten = KONTEN.id AND ARTIST.id = SONG.id_artist AND ARTIST.email_akun = AKUN.email 
    GROUP BY KONTEN.judul, AKUN.nama, KONTEN.tanggal_rilis, SONG.id_konten ORDER BY total_plays DESC LIMIT 20;
    """

    results = execute_raw_query(query)

    result_data = []

    for result in results:
        id_lagu = result[0]
        judul = result[1]
        tanggal_rilis = result[2]
        nama = result[3]
        total_play = result[4]

        result_data.append({
            'id_lagu': id_lagu,
            'judul' : judul,
            'tanggal_rilis': tanggal_rilis,
            'nama': nama,
            'total_play' : total_play
        })
    
    context = {
        'results' : result_data,
        'type' : "daily"
        }
    return render(request, "detail_chart.html", context)

def chart_detail_weekly(request):
    query = """
    SELECT DISTINCT SONG.id_konten, KONTEN.judul, KONTEN.tanggal_rilis, AKUN.nama, COALESCE(COUNT(AKUN_PLAY_SONG.waktu),0 ) AS total_plays
    FROM MARMUT.KONTEN, MARMUT.SONG, MARMUT.AKUN_PLAY_SONG, MARMUT.AKUN, MARMUT.ARTIST WHERE AKUN_PLAY_SONG.waktu >= CURRENT_DATE - INTERVAL '1 weeks' 
    AND SONG.id_konten = AKUN_PLAY_SONG.id_song AND SONG.id_konten = KONTEN.id 
    AND ARTIST.id = SONG.id_artist AND ARTIST.email_akun = AKUN.email 
    GROUP BY KONTEN.judul, AKUN.nama, KONTEN.tanggal_rilis, SONG.id_konten ORDER BY total_plays DESC LIMIT 20;
    """

    results = execute_raw_query(query)

    result_data = []

    for result in results:
        id_lagu = result[0]
        judul = result[1]
        tanggal_rilis = result[2]
        nama = result[3]
        total_play = result[4]

        result_data.append({
            'id_lagu': id_lagu,
            'judul' : judul,
            'tanggal_rilis': tanggal_rilis,
            'nama': nama,
            'total_play' : total_play
        })
    
    context = {
        'results' : result_data,
        'type' : "Weekly"
        }
    return render(request, "detail_chart.html", context)

def chart_detail_monthly(request):
    query = """
    SELECT DISTINCT SONG.id_konten, KONTEN.judul, KONTEN.tanggal_rilis, AKUN.nama, COALESCE(COUNT(AKUN_PLAY_SONG.waktu),0 ) AS total_plays
    FROM MARMUT.KONTEN, MARMUT.SONG, MARMUT.AKUN_PLAY_SONG, MARMUT.AKUN, MARMUT.ARTIST 
    WHERE AKUN_PLAY_SONG.waktu >= CURRENT_DATE - INTERVAL '1 months' 
    AND SONG.id_konten = AKUN_PLAY_SONG.id_song AND SONG.id_konten = KONTEN.id AND ARTIST.id = SONG.id_artist 
    AND ARTIST.email_akun = AKUN.email 
    GROUP BY KONTEN.judul, AKUN.nama, KONTEN.tanggal_rilis, SONG.id_konten ORDER BY total_plays DESC LIMIT 20;
    """
    
    results = execute_raw_query(query)

    result_data = []

    for result in results:
        id_lagu = result[0]
        judul = result[1]
        tanggal_rilis = result[2]
        nama = result[3]
        total_play = result[4]

        result_data.append({
            'id_lagu': id_lagu,
            'judul' : judul,
            'tanggal_rilis': tanggal_rilis,
            'nama': nama,
            'total_play' : total_play
        })
    
    context = {
        'results' : result_data,
        'type' : "Monthly"
        }
    return render(request, "detail_chart.html", context)


def chart_detail_year(request):
    query = """
    SELECT DISTINCT SONG.id_konten, KONTEN.judul, KONTEN.tanggal_rilis, AKUN.nama, COALESCE(COUNT(AKUN_PLAY_SONG.waktu),0 ) AS total_plays
    FROM MARMUT.KONTEN,  MARMUT.SONG,  MARMUT.AKUN_PLAY_SONG,  MARMUT.AKUN,  MARMUT.ARTIST 
    WHERE AKUN_PLAY_SONG.waktu >= CURRENT_DATE - INTERVAL '1 years' 
    AND SONG.id_konten = AKUN_PLAY_SONG.id_song AND SONG.id_konten = KONTEN.id 
    AND ARTIST.id = SONG.id_artist AND ARTIST.email_akun = AKUN.email 
    GROUP BY KONTEN.judul, AKUN.nama, KONTEN.tanggal_rilis, SONG.id_konten ORDER BY total_plays DESC LIMIT 20;
    """

    results = execute_raw_query(query)

    result_data = []

    for result in results:
        id_lagu = result[0]
        judul = result[1]
        tanggal_rilis = result[2]
        nama = result[3]
        total_play = result[4]

        result_data.append({
            'id_lagu': id_lagu,
            'judul' : judul,
            'tanggal_rilis': tanggal_rilis,
            'nama': nama,
            'total_play' : total_play
        })
    
    context = {
        'results' : result_data,
        'type' : "Yearly"
            }
    
    return render(request, "detail_chart.html", context)
