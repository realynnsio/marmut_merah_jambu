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
