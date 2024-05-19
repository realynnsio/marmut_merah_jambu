from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from marmut_merah_jambu.db import fetch
from django.db import connection

# def show_search_bar(request):
#     context = {}
#     return render(request, "search_bar.html", context)

def ke_halaman(request):
    email = request.session.get('email')
    context = {}
    return render(request, 'search.html', context)

def show_search(request):
    email = request.session.get('email')
    hasil = search_data(request)
    context = {
        'data': hasil if hasil else []  # Return an empty list if hasil is None or empty
    }
    return render(request, "search.html", context)

def search_data(request):  
    if request.method == 'GET' and 'search' in request.GET:
        email = request.session.get('email')
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
                WHERE K.judul = %s)
                UNION ALL  
                (SELECT 
                    K.judul, 
                    'Podcast' AS tipe,
                    AK.nama AS oleh
                FROM marmut.KONTEN K
                JOIN marmut.PODCAST P ON K.id = P.id_konten
                JOIN marmut.AKUN AK ON P.email_podcaster = AK.email
                WHERE K.judul = %s)
                """,
                [search_value, search_value]
            )
            result = fetch(cursor)
    else:
        result = []  # Return an empty list if no search query is provided

    return result