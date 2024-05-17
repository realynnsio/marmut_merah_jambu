from django.shortcuts import render
from utils.query import execute_raw_query
from django.db import connection


# Create your views here.
def show_dashboard(request):
    email = request.session.get('email')

    with connection.cursor() as cursor:
        cursor.execute("set search_path to marmut;")
        cursor.execute(get_user(email))
        res = parse(cursor)
    
    gender = ""
    role_string = ""
    
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

def get_user(email):
    return f"""
        SELECT *
        FROM AKUN
        WHERE email = '{email}';
    """

def parse(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]