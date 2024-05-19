def get_user(email):
    return f"""
        SELECT *
        FROM AKUN
        WHERE email = '{email}';
    """

def get_songs(artist_id, songwriter_id):
    return f"""
        (SELECT DISTINCT
            k.judul as judul
        FROM
            KONTEN k
            JOIN SONG s ON s.id_konten = k.id
        WHERE
            s.id_artist = '{artist_id}')
        UNION
        (SELECT DISTINCT
            k.judul as judul
        FROM
            KONTEN k
            JOIN SONG s ON s.id_konten = k.id
            JOIN SONGWRITER_WRITE_SONG sws ON sws.id_song = s.id_konten
        WHERE
            sws.id_songwriter = '{songwriter_id}')
        ;
    """

def get_artist_id(email):
    return f"""
        SELECT id
        FROM ARTIST
        WHERE email_akun = '{email}'
        ;
    """

def get_songwriter_id(email):
    return f"""
        SELECT id
        FROM SONGWRITER
        WHERE email_akun = '{email}'
        ;
    """