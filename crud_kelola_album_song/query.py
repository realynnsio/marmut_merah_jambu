def get_album_query():
    return f"""
        SELECT
            a.judul,
            l.nama,
            a.jumlah_lagu,
            a.total_durasi
        FROM
            ALBUM as a
            JOIN LABEL as l ON a.id_label= l.id
        ;
    """