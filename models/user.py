import database


def get_user_by_email(email):
    results = database.sql_select(
        'SELECT id, password from users WHERE email = %s', [email])
    if len(results):
        result = results[0]
        return result
    else:
        return None


def insert_user(name, email, hashed_password):
    database.sql_write("INSERT into users (name, email, password) VALUES (%s, %s, %s);", [
        name, email, hashed_password
    ])
