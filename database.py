import sqlite3
import random

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
            synopsis TEXT NOT NULL,
            director TEXT,
            comment TEXT
        )
    """)

    conn.commit()
    conn.close()


# INSERT
def insert_movie(title, genre, synopsis, director, comment):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO movies (title, genre, synopsis, director, comment)
        VALUES (?, ?, ?, ?, ?)
    """, (title, genre, synopsis, director, comment))

    conn.commit()
    conn.close()


# RETRIEVE all genre (needed for the genre selected button)
def get_all_genres():
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT genre FROM movies")
    results = cursor.fetchall()

    conn.close()

    # Convert [('Action',), ('Drama',)] → ['Action', 'Drama']
    genres = [row[0] for row in results]
    return genres


# RETRIEVE all movies
def get_all_movies():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT movie_id, title, genre, synopsis, director, comment
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
        SELECT title, synopsis, director, comment
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

# SEARCH BY TITLE
def search_movie_by_title(title):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    query = """
    SELECT title, synopsis
    FROM movies
    WHERE title LIKE ?
    """

    cursor.execute(query, ('%' + title + '%',))

    results = cursor.fetchall()

    conn.close()

    return results

#Random movie recommendation
def get_random_movie():
    
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT title, synopsis
    FROM movies
    ORDER BY RANDOM()
    LIMIT 1
    """)

    movie = cursor.fetchone()

    conn.close()

    return movie

def pimper_ma_base():
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("ALTER TABLE movies ADD COLUMN director TEXT;")
        cursor.execute("ALTER TABLE movies ADD COLUMN comment TEXT;")
        conn.commit()
        print("Colonnes ajoutées avec succès !")
    except sqlite3.OperationalError:
        print("Les colonnes existent déjà ou une erreur est survenue.")
    finally:
        conn.close()

# On l'exécute tout de suite
if __name__ == "__main__":
    pimper_ma_base()