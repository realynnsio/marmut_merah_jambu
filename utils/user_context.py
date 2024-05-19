from marmut_merah_jambu.db import fetch
from django.db import connection

def context_user_getter(request):
    with connection.cursor() as cursor:
        email = request.session.get('email')
        cursor.execute("SELECT COUNT(*) AS pu FROM marmut.premium WHERE email = %s", [email])
        result = fetch(cursor)
        if result[0]['pu'] > 0:
            result1 = True
        else:
            result1 = False
    user = {
        'nama': request.session.get('nama'),
        'email': request.session.get('email'),
        'roles': request.session.get('roles'),
        'status': result1
    }
    return user
