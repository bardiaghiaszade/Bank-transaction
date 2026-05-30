import sqlite3

DB_NAME = "after.db"


def get_users():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM people")
    users = [row[0] for row in cursor.fetchall()]

    conn.close()
    return users


def transfer(sender, receiver, amount):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, money FROM people WHERE name = ?", (sender,))
    s = cursor.fetchone()

    cursor.execute("SELECT id, money FROM people WHERE name = ?", (receiver,))
    r = cursor.fetchone()

    if not s or not r:
        conn.close()
        return "User not found"

    if s[1] < amount:
        conn.close()
        return "Not enough money"

    cursor.execute(
        "UPDATE people SET money = ? WHERE id = ?",
        (s[1] - amount, s[0])
    )

    cursor.execute(
        "UPDATE people SET money = ? WHERE id = ?",
        (r[1] + amount, r[0])
    )

    conn.commit()
    conn.close()

    return "Success"