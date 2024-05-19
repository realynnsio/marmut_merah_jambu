from django.shortcuts import render, redirect, reverse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import uuid
from django.http import HttpResponseRedirect
from main.helper.function import *
import random
from .query import *

# Create your views here.

# R CEK ROYALTI (ARTIST/SONGWRITER & LABEL)
# Fitur ini memungkinkan artist/songwriter/label melihat riwayat royalti
# yang mereka miliki berdasarkan lagu karya mereka. Ketika artist/songwriter/label
# mengakses halaman ini, sistem akan melakukan pembaruan total royalti berdasarkan
# rate royalti dari artist/songwriter/label tersebut * total play lagu.

# INSERT INTO the_table (id, column_1, column_2) 
# VALUES (1, 'A', 'X'), (2, 'B', 'Y'), (3, 'C', 'Z')
# ON CONFLICT (id) DO UPDATE 
#   SET column_1 = excluded.column_1, 
#       column_2 = excluded.column_2;

def show_list_royalti(request):
    email = request.session.get('email')

    royalties = []
    cursor = connection.cursor()
    cursor.execute("set search_path to marmut;")

    if request.session.get('is_artist') and request.session.get('is_songwriter'):
        cursor.execute(get_royalti_both_roles(email))
        res = parse(cursor)
        for item in res:
            royalties.append(item)

            if item.get('artist_phc') != 0:
                id_pemilik_hak_cipta = item.get('artist_phc')
                id_song = item.get('id_song')
                total_royalti = item.get('artist_royalti')
                cursor.execute(
                    f"""
                        INSERT INTO ROYALTI (id_pemilik_hak_cipta, id_song, jumlah) 
                        VALUES ('{id_pemilik_hak_cipta}', '{id_song}', {total_royalti})
                        ON CONFLICT (id_pemilik_hak_cipta, id_song) DO UPDATE 
                        SET jumlah = excluded.jumlah;
                    """
                )
            
            if item.get('songwriter_phc') != 0:
                id_pemilik_hak_cipta = item.get('songwriter_phc')
                id_song = item.get('id_song')
                total_royalti = item.get('songwriter_royalti')
                cursor.execute(
                    f"""
                        INSERT INTO ROYALTI (id_pemilik_hak_cipta, id_song, jumlah) 
                        VALUES ('{id_pemilik_hak_cipta}', '{id_song}', {total_royalti})
                        ON CONFLICT (id_pemilik_hak_cipta, id_song) DO UPDATE 
                        SET jumlah = excluded.jumlah;
                    """
                )

    elif request.session.get('is_artist'):
        cursor.execute(get_royalti_artist(email))
        res = parse(cursor)
        for item in res:
            royalties.append(item)

            id_pemilik_hak_cipta = item.get('id_pemilik_hak_cipta')
            id_song = item.get('id_song')
            total_royalti = item.get('total_royalti')
            cursor.execute(
                f"""
                    INSERT INTO ROYALTI (id_pemilik_hak_cipta, id_song, jumlah) 
                    VALUES ('{id_pemilik_hak_cipta}', '{id_song}', {total_royalti})
                    ON CONFLICT (id_pemilik_hak_cipta, id_song) DO UPDATE 
                      SET jumlah = excluded.jumlah;
                """
            )
    
    elif request.session.get('is_songwriter'):
        cursor.execute(get_royalti_songwriter(email))
        res = parse(cursor)
        for item in res:
            royalties.append(item)

            id_pemilik_hak_cipta = item.get('id_pemilik_hak_cipta')
            id_song = item.get('id_song')
            total_royalti = item.get('total_royalti')
            cursor.execute(
                f"""
                    INSERT INTO ROYALTI (id_pemilik_hak_cipta, id_song, jumlah) 
                    VALUES ('{id_pemilik_hak_cipta}', '{id_song}', {total_royalti})
                    ON CONFLICT (id_pemilik_hak_cipta, id_song) DO UPDATE 
                      SET jumlah = excluded.jumlah;
                """
            )
    
    elif request.session.get('is_label'):
        cursor.execute(get_royalti_label(email))
        res = parse(cursor)
        for item in res:
            royalties.append(item)

            id_pemilik_hak_cipta = item.get('id_pemilik_hak_cipta')
            id_song = item.get('id_song')
            total_royalti = item.get('total_royalti')
            cursor.execute(
                f"""
                    INSERT INTO ROYALTI (id_pemilik_hak_cipta, id_song, jumlah) 
                    VALUES ('{id_pemilik_hak_cipta}', '{id_song}', {total_royalti})
                    ON CONFLICT (id_pemilik_hak_cipta, id_song) DO UPDATE 
                      SET jumlah = excluded.jumlah;
                """
            )

    context = {
        "royalties" : royalties,
    }
    return render(request, "list_royalti.html", context)