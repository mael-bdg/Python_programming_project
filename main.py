import tkinter as tk
from tkinter import ttk
from database import get_movies_by_genre

import sqlite3
import os

# -----------------------------------
# To create the db file from the sql
# -----------------------------------

def init_db():
    db_exists = os.path.exists("movies.db")

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    if not db_exists:
        with open("brouillon.sql", "r") as file:
            cursor.executescript(file.read())
        print("Database created!")

    conn.commit()
    conn.close()

# -------------------------------
# CLASS FOR GUI
# -------------------------------

class MovieApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Recommendation System")
        self.root.geometry("500x400")

        # -------------------------------
        # TITLE
        # -------------------------------
        title = tk.Label(root, text="Movie Recommender", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # -------------------------------
        # GENRE SELECTION
        # -------------------------------
        genre_label = tk.Label(root, text="Select Genre:")
        genre_label.pack()

        # Dropdown (combobox)
        self.genre_var = tk.StringVar()
        self.genre_dropdown = ttk.Combobox(
            root,
            textvariable=self.genre_var,
            values=[
                "Action", "Comedy", "Drama", "Horror", "Sci-Fi",
                "Crime", "Animation", "Thriller", "Western",
                "Fantasy", "Adventure", "War", "Biography"
            ] # Values based on the genres available in brouillon.sql
        )
        self.genre_dropdown.pack(pady=5)

        # -------------------------------
        # BUTTON
        # -------------------------------
        recommend_btn = tk.Button(
            root,
            text="Recommend Movies",
            command=self.show_movies
        )
        recommend_btn.pack(pady=10)

        # -------------------------------
        # RESULT AREA
        # -------------------------------
        self.result_box = tk.Text(root, height=10, width=50)
        self.result_box.pack(pady=10)

    # -------------------------------
    # Modified to retrieve movie titles and synopsis from the database
    # -------------------------------
    def show_movies(self):
        genre = self.genre_var.get()

        # Clear previous results
        self.result_box.delete("1.0", tk.END)

        # Validation
        if genre == "":
            self.result_box.insert(tk.END, "Please select a genre first.")
            return

        # Get movies from database.py
        movies = get_movies_by_genre(genre)

        # If no movies found
        if not movies:
            self.result_box.insert(tk.END, f"No movies found for {genre}.")
            return

        # Display results
        self.result_box.insert(tk.END, f"Movies for {genre}:\n\n")

        # title = movie title
        # synopsis = movie synopsis
        for title, synopsis in movies:
            self.result_box.insert(tk.END, f"🎬 {title}\n")
            self.result_box.insert(tk.END, f"{synopsis}\n\n")


# -------------------------------
# MAIN PROGRAM
# -------------------------------

root = tk.Tk()
init_db()
app = MovieApp(root)
root.mainloop()
