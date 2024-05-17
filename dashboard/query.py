def get_user(email):
    return f"""
        SELECT *
        FROM AKUN
        WHERE email = '{email}';
    """