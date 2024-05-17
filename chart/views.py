from django.shortcuts import render
from utils.query import execute_raw_query


def show_chart(request):
    context = {}
    return render(request, "list_chart.html", context)

def chart_detail_daily(request):
    query = """
    SELECT DISTINCT KONTEN.judul, KONTEN.tanggal_rilis, AKUN.nama, COALESCE(COUNT(AKUN_PLAY_SONG.waktu),0 ) AS total_plays
    FROM MARMUT.KONTEN, MARMUT.SONG, MARMUT.AKUN_PLAY_SONG, MARMUT.AKUN, MARMUT.ARTIST 
    WHERE AKUN_PLAY_SONG.waktu >= CURRENT_DATE - INTERVAL '1 days' 
    AND SONG.id_konten = AKUN_PLAY_SONG.id_song 
    AND SONG.id_konten = KONTEN.id AND ARTIST.id = SONG.id_artist AND ARTIST.email_akun = AKUN.email 
    GROUP BY KONTEN.judul, AKUN.nama, KONTEN.tanggal_rilis ORDER BY total_plays DESC LIMIT 20;
    """

    results = execute_raw_query(query)

    result_data = []

    for result in results:
        judul = result[0]
        tanggal_rilis = result[1]
        nama = result[2]
        total_play = result[3]

        result_data.append({
            'judul' : judul,
            'tanggal_rilis': tanggal_rilis,
            'nama': nama,
            'total_play' : total_play
        })

    print(result_data)

    context = {
        'results' : result_data,
        'type' : "daily"
        }
    return render(request, "detail_chart.html", context)

def chart_detail_weekly(request):
    query = """
    SELECT DISTINCT KONTEN.judul, KONTEN.tanggal_rilis, AKUN.nama, COALESCE(COUNT(AKUN_PLAY_SONG.waktu),0 ) AS total_plays
    FROM MARMUT.KONTEN, MARMUT.SONG, MARMUT.AKUN_PLAY_SONG, MARMUT.AKUN, MARMUT.ARTIST WHERE AKUN_PLAY_SONG.waktu >= CURRENT_DATE - INTERVAL '1 weeks' 
    AND SONG.id_konten = AKUN_PLAY_SONG.id_song AND SONG.id_konten = KONTEN.id 
    AND ARTIST.id = SONG.id_artist AND ARTIST.email_akun = AKUN.email 
    GROUP BY KONTEN.judul, AKUN.nama, KONTEN.tanggal_rilis ORDER BY total_plays DESC LIMIT 20;
    """

    results = execute_raw_query(query)

    result_data = []

    for result in results:
        judul = result[0]
        tanggal_rilis = result[1]
        nama = result[2]
        total_play = result[3]

        result_data.append({
            'judul' : judul,
            'tanggal_rilis': tanggal_rilis,
            'nama': nama,
            'total_play' : total_play
        })

    print(result_data)
    
    context = {
        'results' : result_data,
        'type' : "Weekly"
        }
    return render(request, "detail_chart.html", context)

def chart_detail_monthly(request):
    query = """
    SELECT DISTINCT KONTEN.judul, KONTEN.tanggal_rilis, AKUN.nama, COALESCE(COUNT(AKUN_PLAY_SONG.waktu),0 ) AS total_plays
    FROM MARMUT.KONTEN, MARMUT.SONG, MARMUT.AKUN_PLAY_SONG, MARMUT.AKUN, MARMUT.ARTIST 
    WHERE AKUN_PLAY_SONG.waktu >= CURRENT_DATE - INTERVAL '1 months' 
    AND SONG.id_konten = AKUN_PLAY_SONG.id_song AND SONG.id_konten = KONTEN.id AND ARTIST.id = SONG.id_artist 
    AND ARTIST.email_akun = AKUN.email 
    GROUP BY KONTEN.judul, AKUN.nama, KONTEN.tanggal_rilis ORDER BY total_plays DESC LIMIT 20;
    """

    results = execute_raw_query(query)

    result_data = []

    for result in results:
        judul = result[0]
        tanggal_rilis = result[1]
        nama = result[2]
        total_play = result[3]

        result_data.append({
            'judul' : judul,
            'tanggal_rilis': tanggal_rilis,
            'nama': nama,
            'total_play' : total_play
        })

    print(result_data)
    
    context = {
        'results' : result_data,
        'type' : "Monthly"
        }
    return render(request, "detail_chart.html", context)


def chart_detail_year(request):
    query = """
    SELECT DISTINCT KONTEN.judul, KONTEN.tanggal_rilis, AKUN.nama, COALESCE(COUNT(AKUN_PLAY_SONG.waktu),0 ) AS total_plays
    FROM MARMUT.KONTEN,  MARMUT.SONG,  MARMUT.AKUN_PLAY_SONG,  MARMUT.AKUN,  MARMUT.ARTIST 
    WHERE AKUN_PLAY_SONG.waktu >= CURRENT_DATE - INTERVAL '1 years' 
    AND SONG.id_konten = AKUN_PLAY_SONG.id_song AND SONG.id_konten = KONTEN.id 
    AND ARTIST.id = SONG.id_artist AND ARTIST.email_akun = AKUN.email 
    GROUP BY KONTEN.judul, AKUN.nama, KONTEN.tanggal_rilis ORDER BY total_plays DESC LIMIT 20;
    """

    results = execute_raw_query(query)

    result_data = []

    for result in results:
        judul = result[0]
        tanggal_rilis = result[1]
        nama = result[2]
        total_play = result[3]

        result_data.append({
            'judul' : judul,
            'tanggal_rilis': tanggal_rilis,
            'nama': nama,
            'total_play' : total_play
        })

    print(result_data)
    
    context = {
        'results' : result_data,
        'type' : "Yearly"
            }
    
    return render(request, "detail_chart.html", context)
