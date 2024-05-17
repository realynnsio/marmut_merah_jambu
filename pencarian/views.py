from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from marmut_merah_jambu.db import fetch
from django.db import connection
from utils.user_context import context_user_getter

# def show_search_bar(request):
#     context = {}
#     return render(request, "search_bar.html", context)

def ke_halaman(request):
    context = {}
    return render(request, 'search.html', context)

def show_search(request):
    hasil = search_data(request)
    context = {
        'data': hasil
    }
    print(context)
    return render(request, "search.html", context)

def search_data(request):  
    if request.method == 'GET' and 'search' in request.GET:
        search_value = request.GET.get('search', None)

        with connection.cursor() as cursor:
            cursor.execute(
                """
                (SELECT 
                    K.judul, 
                    'Song' AS tipe,
                    A.nama AS oleh
                FROM marmut.KONTEN K
                JOIN marmut.SONG S ON K.id = S.id_konten
                JOIN marmut.ARTIST AR ON S.id_artist = AR.id
                JOIN marmut.AKUN A ON AR.email_akun = A.email
                WHERE LOWER(K.judul) LIKE LOWER(%s) OR LOWER(a.nama) LIKE LOWER(%s))
                UNION ALL  
                (SELECT 
                    K.judul, 
                    'Podcast' AS tipe,
                    AK.nama AS oleh
                FROM marmut.KONTEN K
                JOIN marmut.PODCAST P ON K.id = P.id_konten
                JOIN marmut.AKUN AK ON P.email_podcaster = AK.email
                WHERE LOWER(K.judul) LIKE LOWER(%s) OR LOWER(AK.nama) LIKE LOWER(%s))
                UNION ALL
                (SELECT
                    UP.judul,
                    'User Playlist' AS tipe,
                    AKN.nama AS oleh
                FROM marmut.user_playlist UP
                JOIN marmut.AKUN AKN ON UP.email_pembuat = AKN.email
                WHERE LOWER(UP.judul) LIKE LOWER(%s) OR LOWER(AKN.nama) LIKE LOWER(%s))
                """,
                ["%" + search_value + "%", "%" + search_value + "%", "%" + search_value + "%", "%" + search_value + "%", "%" + search_value + "%", "%" + search_value + "%"]
            )
            result = fetch(cursor)
    else:
        result = []  # Return an empty list if no search query is provided
        print(result)
    return result