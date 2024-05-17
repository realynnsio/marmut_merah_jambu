from django.shortcuts import redirect, render
from django.db import connection
from django.urls import reverse
from marmut_merah_jambu.db import fetch

def download_list(request):
    context = {}
    return render(request, "list_download.html", context)

def get_downloaded_songs():
    query = """
    SELECT ds.id_Song AS id,
           k.judul AS judul_lagu,
           a.nama AS nama_artis
    FROM marmut.downloaded_song ds
    JOIN marmut.KONTEN k ON ds.id_song = k.id
    JOIN marmut.SONG s ON s.id_konten = k.id
    JOIN marmut.ARTIST ar ON s.id_artist = ar.id
    JOIN marmut.AKUN a ON ar.email_akun = a.email
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = fetch(cursor)
    return result

def download_list(request):
    downloaded_songs = get_downloaded_songs()
    context = {
        'downloaded_songs': downloaded_songs
    }
    return render(request, "list_download.html", context)


def delete_song(request):
    id_song = request.GET.get('id_song', None)
    # Lakukan operasi penghapusan data
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM marmut.downloaded_song WHERE id_song = %s", (id_song,))
    return redirect(reverse('download_song:download_list'))