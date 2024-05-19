def get_royalti_artist(email):
    return f"""
        WITH artist_info AS (
            SELECT a.id, phc.rate_royalti, a.id_pemilik_hak_cipta
            FROM
                ARTIST a
                JOIN PEMILIK_HAK_CIPTA phc ON phc.id = a.id_pemilik_hak_cipta
                WHERE a.email = '{email}'
        ), song_info AS (
            SELECT s.id_artist, k.judul as judul_lagu, al.judul as judul_album, s.total_play, s.total_download, s.id_konten as id_song
            FROM
                SONG s
                JOIN KONTEN k ON s.id_konten = k.id
                JOIN ALBUM as al ON al.id = s.id_album
        )
        SELECT
            ai.id_pemilik_hak_cipta
            si.judul_lagu,
            si.judul_album,
            si.total_play,
            si.total_download,
            si.id_song,
            (ai.rate_royalti * si.total_play) as total_royalti
        FROM
            artist_info ai
            JOIN song_info si ON si.id_artist = ai.id
        ;
    """

def get_royalti_songwriter(email):
    return f"""
        WITH songwriter_info AS (
            SELECT sw.id, phc.rate_royalti. sw.id_pemilik_hak_cipta
            FROM
                SONGWRITER sw
                JOIN PEMILIK_HAK_CIPTA phc ON phc.id = sw.id_pemilik_hak_cipta
                WHERE sw.email_akun = '{email}'
        ), song_info AS (
            SELECT sws.id_songwriter, k.judul as judul_lagu, al.judul as judul_album, s.total_play, s.total_download, s.id_konten as id_song
            FROM
                SONG s
                JOIN KONTEN k ON s.id_konten = k.id
                JOIN ALBUM as al ON al.id = s.id_album
                JOIN SONGWRITER_WRITE_SONG sws ON sws.id_song = s.id_konten
        )
        SELECT
            swi.id_pemilik_hak_cipta
            si.judul_lagu,
            si.judul_album,
            si.total_play,
            si.total_download,
            si.id_song,
            (swi.rate_royalti * si.total_play) as total_royalti
        FROM
            songwriter_info swi
            JOIN song_info si ON si.id_songwriter = swi.id
        ;
    """

def get_royalti_both_roles(email):
    return f"""
        WITH artist_info AS (
            SELECT a.id AS artist_id, phc.rate_royalti AS artist_rate_royalti, a.id_pemilik_hak_cipta as artist_phc
            FROM ARTIST a
            JOIN PEMILIK_HAK_CIPTA phc ON phc.id = a.id_pemilik_hak_cipta
            WHERE a.email = '{email}'
        ), songwriter_info AS (
            SELECT sw.id AS songwriter_id, phc.rate_royalti AS songwriter_rate_royalti, sw.id_pemilik_hak_cipta as songwriter_phc
            FROM SONGWRITER sw
            JOIN PEMILIK_HAK_CIPTA phc ON phc.id = sw.id_pemilik_hak_cipta
            WHERE sw.email_akun = '{email}'
        ), artist_songs AS (
            SELECT ai.artist_phc, s.id_konten, k.judul AS judul_lagu, al.judul AS judul_album, s.total_play, s.total_download, (ai.artist_rate_royalti * s.total_play) AS total_royalti
            FROM SONG s
            JOIN KONTEN k ON s.id_konten = k.id
            JOIN ALBUM al ON al.id = s.id_album
            JOIN artist_info ai ON s.id_artist = ai.artist_id
        ), songwriter_songs AS (
            SELECT swi.songwriter_phc, s.id_konten, k.judul AS judul_lagu, al.judul AS judul_album, s.total_play, s.total_download, (swi.songwriter_rate_royalti * s.total_play) AS total_royalti
            FROM SONG s
            JOIN KONTEN k ON s.id_konten = k.id
            JOIN ALBUM al ON al.id = s.id_album
            JOIN SONGWRITER_WRITE_SONG sws ON sws.id_song = s.id_konten
            JOIN songwriter_info swi ON sws.id_songwriter = swi.songwriter_id
        )
        SELECT
            COALESCE(asi.artist_phc, 0) AS artist_phc,
            COALESCE(ssi.songwriter_phc, 0) AS songwriter_phc,
            COALESCE(asi.id_konten, ssi.id_konten) AS id_song,
            COALESCE(asi.judul_lagu, ssi.judul_lagu) AS judul_lagu,
            COALESCE(asi.judul_album, ssi.judul_album) AS judul_album,
            COALESCE(asi.total_play, ssi.total_play) AS total_play,
            COALESCE(asi.total_download, ssi.total_download) AS total_download,
            COALESCE(asi.total_royalti, 0) AS artist_royalti,
            COALESCE(ssi.total_royalti, 0) AS songwriter_royalti,
            COALESCE(asi.total_royalti, 0) + COALESCE(ssi.total_royalti, 0) AS total_royalti
        FROM artist_songs asi
        FULL OUTER JOIN songwriter_songs ssi ON asi.id_konten = ssi.id_konten
        ;
    """

def get_royalti_label(email):
    return f"""
        WITH label_info AS (
            SELECT l.id, phc.rate_royalti, l.id_pemilik_hak_cipta
            FROM
                LABEL l
                JOIN PEMILIK_HAK_CIPTA phc ON phc.id = l.id_pemilik_hak_cipta
                WHERE l.email = '{email}'
        ), song_info AS (
            SELECT al.id_label, k.judul as judul_lagu, al.judul as judul_album, s.total_play, s.total_download, s.id_konten as id_song
            FROM
                SONG s
                JOIN KONTEN k ON s.id_konten = k.id
                JOIN ALBUM as al ON al.id = s.id_album
        )
        SELECT
            li.id_pemilik_hak_cipta,
            si.judul_lagu,
            si.judul_album,
            si.total_play,
            si.total_download,
            si.id_song,
            (li.rate_royalti * si.total_play) as total_royalti
        FROM
            label_info li
            JOIN song_info si ON si.id_label = li.id
        ;
    """