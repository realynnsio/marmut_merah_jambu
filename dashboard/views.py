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
    
    gender = ""
    role_string = ""
    
    if not request.session.get('is_label'):
        if res[0].get('gender') == 0:
            gender = "Perempuan"
        else:
            gender = "Laki-Laki"
        
        if request.session.get('is_artist'):
            role_string += "Artist \n"
        if request.session.get('is_songwriter'):
            role_string += "Songwriter \n"
        if request.session.get('is_podcaster'):
            role_string += "Podcaster \n"

    context = {
        "user" : res[0],
        "gender" : gender,
        "roles" : role_string,
    }
    return render(request, "dashboard.html", context)
