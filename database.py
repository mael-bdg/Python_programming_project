import sqlite3

DB_NAME = "movies.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


# CREATE
def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT NOT NULL,
            synopsis TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# INSERT
def insert_movie(title, genre, synopsis):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO movies (title, genre, synopsis)
        VALUES (?, ?, ?)
    """, (title, genre, synopsis))

    conn.commit()
    conn.close()


# RETRIEVE all movies
def get_all_movies():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT movie_id, title, genre, synopsis
        FROM movies
    """)

    movies = cursor.fetchall()
    conn.close()
    return movies


# RETRIEVE by genre
def get_movies_by_genre(genre):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, synopsis
        FROM movies
        WHERE genre = ?
    """, (genre,))

    movies = cursor.fetchall()
    conn.close()
    return movies


# UPDATE
def update_movie(movie_id, title, genre, synopsis):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE movies
        SET title = ?, genre = ?, synopsis = ?
        WHERE movie_id = ?
    """, (title, genre, synopsis, movie_id))

    conn.commit()
    conn.close()


# DELETE
def delete_movie(movie_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM movies
        WHERE movie_id = ?
    """, (movie_id,))

    conn.commit()
    conn.close()