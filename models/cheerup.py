import database


# Insert cheerup into DB
def insert_cheerup(body, user_id):
    database.sql_write(
        "INSERT into cheerups (body, user_id) VALUES (%s, %s);", [body, user_id])


# Select all cheerups from DB
def get_all_cheerups():
    results = database.sql_select(
        "SELECT cheerups.id, cheerups.body, cheerups.user_id, users.name from cheerups INNER JOIN users ON users.id = cheerups.user_id", [])
    return results

# Select single cheer from cheerups


def get_cheer(id):
    results = database.sql_select(
        "SELECT id, body, user_id from cheerups WHERE id = %s", [id])
    result = results[0]
    return result


# Update cheer
def update_cheer(id, body, user_id):
    database.sql_write("UPDATE cheerups set body = %s WHERE id = %s", [
                       body, id])


# Delete cheer from DB
def delete_cheer(id):
    database.sql_write("DELETE from cheerups where id = %s", [id])
