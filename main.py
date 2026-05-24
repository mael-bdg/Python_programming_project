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

        # SEARCH BAR
        search_label = tk.Label(top_frame, text="Search Title:", bg="#8FA1AF")
        search_label.grid(row=1, column=0, padx=5, pady=10)
        
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(top_frame, textvariable=self.search_var)
        search_entry.grid(row=1, column=1, padx=5)
        search_btn = tk.Button(
            top_frame,
            text="Search",
            command=self.search_movie
        )
        search_btn.grid(row=1, column=2, padx=10)

        # -------------------------------
        # BUTTON (same row)
        # -------------------------------

        recommend_btn = tk.Button(
            top_frame,
            text="Recommend Movies",
            command=self.show_movies,
            bg="#4A90E2",
            fg="white",
            font=("Arial", 10, "bold")
        )
        recommend_btn.grid(row=0, column=2, padx=10)

        random_btn = tk.Button(
         top_frame,
         text="🎲 Surprise Me",
         command=self.random_movie,
         bg="#4A90E2",
         fg="white",
         font=("Arial", 10, "bold")
        )

        random_btn.grid(row=2, column=1, pady=10)

        # -------------------------------
        # RESULT AREA
        # -------------------------------
        frame = tk.Frame(root)
        frame.pack(pady=15)

        scrollbar = tk.Scrollbar(frame)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.result_box = tk.Text(
         frame,
         height=25,
         width=80,
         font=("Arial", 11),
         bg="#F5F5F5",
         fg="#222222"
        )

        self.result_box.pack(side=tk.LEFT)

        scrollbar.config(command=self.result_box.yview)

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
        try:
         movies = database.get_movies_by_genre(genre)

        except Exception as e:
         self.result_box.insert(tk.END, f"Database Error: {e}")
         return

        # Display results
        self.result_box.insert(tk.END, f"Movies for {genre}:\n\n")
        for title, synopsis in movies:
            self.result_box.insert(tk.END, f"- {title}\n")
            self.result_box.insert(tk.END, f"  {synopsis}\n\n")
    
    def search_movie(self):
        title = self.search_var.get()
        
        self.result_box.delete("1.0", tk.END)
        
        if title == "":
            self.result_box.insert(tk.END, "Please enter a movie title.")
        return

        try:
         movies = database.search_movie_by_title(title)

         if not movies:
            self.result_box.insert(
                tk.END,
                "No movie found."
            )
            return

         for title, synopsis in movies:
            self.result_box.insert(tk.END, f"{title}\n")
            self.result_box.insert(tk.END, f"{synopsis}\n\n")

        except Exception as e:
         self.result_box.insert(tk.END, f"Error: {e}")
    
    def random_movie(self):
    
     self.result_box.delete("1.0", tk.END)

     try:
        movie = database.get_random_movie()

        if movie:
            title, synopsis = movie

            self.result_box.insert(tk.END, f"{title}\n\n")
            self.result_box.insert(tk.END, f"{synopsis}")

     except Exception as e:
        self.result_box.insert(tk.END, f"Error: {e}")


# -------------------------------
# MAIN PROGRAM
# -------------------------------

root = tk.Tk()
init_db()
app = MovieApp(root)
root.mainloop()
