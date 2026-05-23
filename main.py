import tkinter as tk
from tkinter import ttk

import database

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
        self.root.geometry("800x600")
        self.root.configure(bg="#8FA1AF")

        # -------------------------------
        # TITLE
        # -------------------------------
        title = tk.Label(root, text="Movie Recommender", font=("Helvetica", 16, "bold"), bg="#8FA1Af")
        title.pack(pady=15)

        # -------------------------------
        # GENRE SELECTION
        # -------------------------------
        top_frame = tk.Frame(root, bg="#8FA1AF")
        top_frame.pack(pady=10)

        # Label
        genre_label = tk.Label(top_frame, text="Select Genre:", bg="#8FA1AF")
        genre_label.grid(row=0, column=0, padx=5)

        # Dropdown 
        genres = database.get_all_genres()
        self.genre_var = tk.StringVar()
        self.genre_dropdown = ttk.Combobox(
            top_frame,
            textvariable=self.genre_var,
            values=genres
        )
        self.genre_dropdown.grid(row=0, column=1, padx=5)

        # -------------------------------
        # BUTTON (same row)
        # -------------------------------

        recommend_btn = tk.Button(
            top_frame,
            text="Recommend Movies",
            command=self.show_movies
        )
        recommend_btn.grid(row=0, column=2, padx=10)

        # -------------------------------
        # RESULT AREA
        # -------------------------------
        self.result_box = tk.Text(root, height=25, width=80)
        self.result_box.pack(pady=15)

    # -------------------------------
    # SHOW MOVIES
    # -------------------------------
    def show_movies(self):
        genre = self.genre_var.get()

        # Clear previous results
        self.result_box.delete("1.0", tk.END)

        # Validation
        if genre == "":
            self.result_box.insert(tk.END, "Please select a genre first.")
            return

        # Get movies
        movies = database.get_movies_by_genre(genre)

        # Display results
        self.result_box.insert(tk.END, f"Movies for {genre}:\n\n")
        for title, synopsis in movies:
            self.result_box.insert(tk.END, f"- {title}\n")
            self.result_box.insert(tk.END, f"  {synopsis}\n\n")


# -------------------------------
# MAIN PROGRAM
# -------------------------------

root = tk.Tk()
init_db()
app = MovieApp(root)
root.mainloop()
