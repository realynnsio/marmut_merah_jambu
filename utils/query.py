from django.db import connection

def execute_raw_query(query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        result = cursor.fetchall()
    return result