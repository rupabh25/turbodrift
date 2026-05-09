import sqlite3
import bcrypt

# ---------- DATABASE ----------
def create_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password BLOB,
            role TEXT
        )
    """)

    # default admin
    admin_password = bcrypt.hashpw(
        "admin123".encode(),
        bcrypt.gensalt()
    )

    c.execute("""
        INSERT OR IGNORE INTO users(id, username, password, role)
        VALUES (1, ?, ?, ?)
    """, ("admin", admin_password, "admin"))

    conn.commit()
    conn.close()

# ---------- LOGIN ----------
def login_user(username, password):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()

    conn.close()

    if user:
        stored_password = user[2]

        if bcrypt.checkpw(password.encode(), stored_password):
            return user

    return None

# ---------- SIGNUP ----------
def signup_user(username, password):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    try:
        c.execute("""
            INSERT INTO users(username,password,role)
            VALUES (?,?,?)
        """, (username, hashed_password, "user"))

        conn.commit()

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()

    return True
