from django.shortcuts import render, redirect, reverse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import uuid
from django.http import HttpResponseRedirect
from main.helper.function import *
from cru_registrasi.query import *


# Create your views here.
def show_registration_menu(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }
    return render(request, "registration_menu.html", context)

def registration_user_form(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }
    return render(request, "registration_user_form.html", context)

def registration_label_form(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }
    return render(request, "registration_label_form.html", context)

def login_form(request):
    context = {}
    return render(request, "login.html", context)

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        nama = request.POST.get('nama')
        gender = request.POST.get('gender')
        tempat_lahir = request.POST.get('tempat_lahir')
        tanggal_rilis = request.POST.get('tanggal_lahir')
        kota_asal = request.POST.get("kota_asal")
        roles = request.POST.getlist("role")
        if (roles) :
            is_verified = True
        else:
            is_verified = False

        if (not (email and password and nama and gender and tempat_lahir and tanggal_rilis and kota_asal)):
            context = {'message': "Harap isi data dengan benar!",
                    'gagal': True}
            return render(request, 'registration_menu.html', context)
        else :
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT COUNT(*) FROM MARMUT.AKUN WHERE email = '{email}'")
                row = cursor.fetchone()
                email_exists = row[0] > 0

                if email_exists:
                    context = {'message': "Email sudah terdaftar!",
                                'gagal': True}
                    return render(request, 'registration_menu.html', context)
                else :
                    query = f"""
                            INSERT INTO MARMUT.AKUN VALUES ('{email}', '{password}', '{nama}', '{gender}', '{tempat_lahir}', '{tanggal_rilis}', '{is_verified}', '{kota_asal}')
                            """
                    
                    with connection.cursor() as cursor:
                        cursor.execute(query)

                    if (is_verified):

                        id_pemilik_hak_cipta = uuid.uuid4()

                        query4 = f"""
                                INSERT INTO MARMUT.PEMILIK_HAK_CIPTA VALUES ('{id_pemilik_hak_cipta}', 5000000)
                                """
                                
                        with connection.cursor() as cursor:
                            cursor.execute(query4)

                        for role in roles:
                            if (role == "podcaster"):
                        
                                query2 = f"""
                                    INSERT INTO MARMUT.PODCASTER VALUES ('{email}')
                                    """
                                
                                with connection.cursor() as cursor:
                                    cursor.execute(query2)
                            
                            elif (role == "artist"):

                                id_artist = uuid.uuid4()

                                query3 = f"""
                                    INSERT INTO MARMUT.ARTIST VALUES ('{id_artist}', '{email}', '{id_pemilik_hak_cipta}')
                                    """
                                
                                with connection.cursor() as cursor:
                                    cursor.execute(query3)
                                
                            else :

                                id_songwriter = uuid.uuid4()
                                query5 = f"""
                                    INSERT INTO MARMUT.SONGWRITER VALUES ('{id_songwriter}', '{email}', '{id_pemilik_hak_cipta}')
                                    """
                                
                                with connection.cursor() as cursor:
                                    cursor.execute(query5)
                                    
                            
                    return HttpResponseRedirect(reverse('cru_registrasi:login_form'))

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not (email and password):
            context = {'message': "Email dan password harus diisi!", 'gagal': True}
            return render(request, 'login_form.html', context)

        query = f"""
        SELECT COUNT(*)
        FROM MARMUT.AKUN
        WHERE email = '{email}' AND password = '{password}'
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchone()
            user_exists = row[0] > 0

        if user_exists:
            request.session['email'] = email  

            query2 = f"""
                    SELECT COUNT(*) FROM MARMUT.ARTIST, MARMUT.AKUN WHERE email = email_akun AND email_akun = '{email}' 
                    """
            
            with connection.cursor() as cursor:
                cursor.execute(query2)
                row = cursor.fetchone()
                is_artist = row[0] > 0

            if is_artist:
                request.session['is_artist'] = True
            else:
                request.session['is_artist'] = False
            
            query3 = f"""
                    SELECT COUNT(*) FROM MARMUT.PODCASTER, MARMUT.AKUN WHERE PODCASTER.email = AKUN.email AND PODCASTER.email = '{email}' 
                    """
            
            with connection.cursor() as cursor:
                cursor.execute(query3)
                row = cursor.fetchone()
                is_podcaster = row[0] > 0

            if is_podcaster:
                request.session['is_podcaster'] = True
            else:
                request.session['is_podcaster'] = False
            
            query4 = f"""
                    SELECT COUNT(*) FROM MARMUT.SONGWRITER, MARMUT.AKUN WHERE email_akun = AKUN.email AND email_akun = '{email}' 
                    """
            
            with connection.cursor() as cursor:
                cursor.execute(query4)
                row = cursor.fetchone()
                is_songwriter = row[0] > 0

            if is_songwriter:
                request.session['is_songwriter'] = True
            else:
                request.session['is_songwriter'] = False

            return HttpResponseRedirect(reverse('dashboard:show_dashboard')) 
        else:
            context = {'message': "Email atau password salah!", 'gagal': True}
            return render(request, 'login_form.html', context)
    else:
        return render(request, 'login_form.html')
       

