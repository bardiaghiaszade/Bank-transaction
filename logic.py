
import sqlite3
import os

DB_NAME = os.path.join(os.path.dirname(__file__), "database.db")


def get_users():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM people")
    users = [row[0] for row in cursor.fetchall()]

    conn.close()
    return users


def get_balance(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT money FROM people WHERE name = ?", (name,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return None


def add_user(name):
    name = name.strip()

    if not name:
        return "Name cannot be empty"

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM people WHERE name = ?", (name,))
    existing_user = cursor.fetchone()

    if existing_user:
        conn.close()
        return "User already exists"

    cursor.execute(
        "INSERT INTO people (name, money) VALUES (?, ?)",
        (name, 100)
    )

    conn.commit()
    conn.close()

    return "Success"


def transfer(sender, receiver, amount):
    if sender == receiver:
        return "Sender and receiver must be different"

    if amount <= 0:
        return "Amount must be greater than zero"

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, money FROM people WHERE name = ?", (sender,)
    )
    s = cursor.fetchone()

    cursor.execute(
        "SELECT id, money FROM people WHERE name = ?", (receiver,)
    )
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
