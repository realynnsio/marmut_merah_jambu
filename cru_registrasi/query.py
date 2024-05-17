def is_user_artist(email):
    return f"""
        SELECT *
        FROM ARTIST
        WHERE email_akun = '{email}'
        ;
    """

def is_user_songwriter(email):
    return f"""
        SELECT *
        FROM SONGWRITER
        WHERE email_akun = '{email}'
        ;
    """

def is_user_podcaster(email):
    return f"""
        SELECT *
        FROM PODCASTER
        WHERE email = '{email}'
        ;
    """

def is_user_premium(email):
    return f"""
        SELECT *
        FROM PREMIUM
        WHERE email = '{email}'
        ;
    """

def is_user_label(email):
    return f"""
        SELECT *
        FROM LABEL
        WHERE email = '{email}'
        ;
    """

# Spesifikasi Navbar Pengguna (Sudah Login)
# Dashboard
# [Jika Pengguna Biasa/Artist/Songwriter/Podcaster] Chart
# [Jika Pengguna Biasa/Artist/Songwriter/Podcaster] Search Bar
# [Jika Pengguna Biasa/Artist/Songwriter/Podcaster] Kelola Playlist
# [Jika Pengguna Biasa/Artist/Songwriter/Podcaster] Langganan Paket
# [Jika Premium] Kelola Downloaded Songs
# [Jika Podcaster] Kelola Podcast
# [Jika Artist/Songwriter] Kelola Album & Songs
# [Jika Label] Kelola Album
# [Jika Artist/Songwriter/Label] Cek Royalti
# Logout
