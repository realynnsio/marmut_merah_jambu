def get_artist_nama(email):
    return f"""
        SELECT a.nama
        FROM ARTIST as ar JOIN AKUN as a ON ar.email_akun = a.email
        WHERE ar.email_akun = '{email}'
        ;
    """

def get_songwriter_nama(email):
    return f"""
        SELECT akun.nama
        FROM SONGWRITER JOIN AKUN ON SONGWRITER.email_akun = AKUN.email
        WHERE SONGWRITER.email_akun = '{email}'
        ;
    """

def get_artist_id(email):
    return f"""
        SELECT id
        FROM ARTIST
        WHERE email_akun = '{email}'
        ;
    """

def get_artist_albums(id):
    return f"""
        SELECT DISTINCT
            a.id,
            a.judul,
            l.nama,
            a.jumlah_lagu,
            a.total_durasi
        FROM
            SONG as s
            JOIN ALBUM as a ON s.id_album = a.id
            JOIN LABEL as l ON a.id_label = l.id
        WHERE
            s.id_artist = '{id}'
        ;
    """

def get_songwriter_id(email):
    return f"""
        SELECT id
        FROM SONGWRITER
        WHERE email_akun = '{email}'
        ;
    """

def get_songwriter_albums(id):
    return f"""
        SELECT DISTINCT
            a.id,
            a.judul,
            l.nama,
            a.jumlah_lagu,
            a.total_durasi
        FROM
            SONGWRITER_WRITE_SONG as sws
            JOIN SONG as s ON sws.id_song = s.id_konten
            JOIN ALBUM as a ON s.id_album = a.id
            JOIN LABEL as l ON a.id_label = l.id
        WHERE
            sws.id_songwriter = '{id}'
        ;
    """

def get_artist_songwriter_albums(id):
    return f"""
        (SELECT DISTINCT
            a.id,
            a.judul,
            l.nama,
            a.jumlah_lagu,
            a.total_durasi
        FROM
            SONG as s
            JOIN ALBUM as a ON s.id_album = a.id
            JOIN LABEL as l ON a.id_label = l.id
        WHERE
            s.id_artist = '{id}')
        UNION
        (SELECT DISTINCT
            a.id,
            a.judul,
            l.nama,
            a.jumlah_lagu,
            a.total_durasi
        FROM
            SONGWRITER_WRITE_SONG as sws
            JOIN SONG as s ON sws.id_song = s.id_konten
            JOIN ALBUM as a ON s.id_album = a.id
            JOIN LABEL as l ON a.id_label = l.id
        WHERE
            sws.id_songwriter = '{id}')
        ;
    """