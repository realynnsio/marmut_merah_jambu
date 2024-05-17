from django.shortcuts import redirect, render
from django.db import connection
from django.urls import reverse
from marmut_merah_jambu.db import fetch
from utils.user_context import context_user_getter


def get_downloaded_songs(request):
    user = context_user_getter(request)
    email = user.get('email')
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT ds.id_Song AS id,
                k.judul AS judul_lagu,
                a.nama AS nama_artis
            FROM marmut.downloaded_song ds
            JOIN marmut.KONTEN k ON ds.id_song = k.id
            JOIN marmut.SONG s ON s.id_konten = k.id
            JOIN marmut.ARTIST ar ON s.id_artist = ar.id
            JOIN marmut.AKUN a ON ar.email_akun = a.email
            WHERE ds.email_downloader = %s
            """, [email] )
        result = fetch(cursor)
    return result

def download_list(request):
    downloaded_songs = get_downloaded_songs(request)
    context = {
        'downloaded_songs': downloaded_songs
    }
    return render(request, "list_download.html", context)


def delete_song(request):
    user = context_user_getter(request)
    email= user.get('email')
    id_song = request.GET.get('id_song', None)
    # Lakukan operasi penghapusan data
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM marmut.downloaded_song WHERE id_song = %s AND email_downloader = %s", (id_song,email))
        cursor.execute("UPDATE marmut.SONG SET total_download = GREATEST(total_download - 1, 0) WHERE SONG.id_konten = %s;", [id_song])
    return redirect(reverse('downloaded_songs:download_list'))