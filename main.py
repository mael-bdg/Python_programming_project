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
        self.root.geometry("900x700")
        
        self.bg_dark = "#141A29"       # Fond principal (Bleu très sombre/Noir)
        self.bg_card = "#1F293D"       # Fond des panneaux/cartes
        self.fg_light = "#FFFFFF"      # Texte principal
        self.fg_muted = "#9CA3AF"      # Texte secondaire (Gris)
        self.accent_color = "#00D2C4"  # Couleur d'accentuation (Cyan néon)
        self.btn_bg = "#2563EB"        # Bleu intense pour les boutons d'action

        self.root.configure(bg=self.bg_dark)

        # Configuration des styles TTK pour les Combobox et Scrollbars
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TCombobox", fieldbackground=self.bg_card, background=self.bg_card, foreground=self.fg_light)
        
        # --- EN-TÊTE (HEADER) ---
        header_frame = tk.Frame(root, bg=self.bg_dark)
        header_frame.pack(fill=tk.X, padx=30, pady=20)

        # -------------------------------
        # TITLE
        # -------------------------------
        title = tk.Label(
            header_frame, 
            text="🎬 CineMatch", 
            font=("Helvetica", 24, "bold"), 
            bg=self.bg_dark, 
            fg=self.accent_color
        )
        title.pack(side=tk.LEFT)
        subtitle = tk.Label(
            header_frame, 
            text="Your next cinematic journey starts here", 
            font=("Helvetica", 11, "italic"), 
            bg=self.bg_dark, 
            fg=self.fg_muted
        )
        subtitle.pack(side=tk.LEFT, padx=15, pady=10)

        # --- PANNEAU DE CONTRÔLE (SIDEBAR / TOP BAR MIX) ---
        control_panel = tk.Frame(root, bg=self.bg_card, bd=0, highlightthickness=0)
        control_panel.pack(fill=tk.X, padx=30, pady=10, ipady=15)

        # Grille interne pour aligner proprement les éléments
        control_panel.columnconfigure((0, 1, 2, 3), weight=1)

        # Section Recherche par titre
        search_frame = tk.Frame(control_panel, bg=self.bg_card)
        search_frame.grid(row=0, column=0, columnspan=2, padx=20, sticky="ew")
        
        search_label = tk.Label(search_frame, text="SEARCH BY TITLE", font=("Helvetica", 9, "bold"), bg=self.bg_card, fg=self.fg_muted)
        search_label.pack(anchor="w", pady=(5, 2))
        
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(
            search_frame, 
            textvariable=self.search_var, 
            bg=self.bg_dark, 
            fg=self.fg_light, 
            insertbackground=self.fg_light,
            bd=0, 
            highlightthickness=1, 
            highlightbackground="#374151",
            highlightcolor=self.accent_color,
            font=("Helvetica", 11)
        )
        search_entry.pack(fill=tk.X, ipady=6, side=tk.LEFT, expand=True)

        search_btn = tk.Button(
            search_frame,
            text="🔍",
            command=self.search_movie,
            bg=self.btn_bg,
            fg=self.fg_light,
            activebackground=self.accent_color,
            activeforeground=self.bg_dark,
            font=("Helvetica", 11, "bold"),
            bd=0,
            cursor="hand2",
            padx=15
        )
        search_btn.pack(side=tk.LEFT, padx=(5, 0), ipady=4)

        # Section Filtrer par Genre
        genre_frame = tk.Frame(control_panel, bg=self.bg_card)
        genre_frame.grid(row=0, column=2, padx=20, sticky="ew")

        genre_label = tk.Label(genre_frame, text="FILTER BY GENRE", font=("Helvetica", 9, "bold"), bg=self.bg_card, fg=self.fg_muted)
        genre_label.pack(anchor="w", pady=(5, 2))

        genres = database.get_all_genres()
        self.genre_var = tk.StringVar()
        self.genre_dropdown = ttk.Combobox(
            genre_frame,
            textvariable=self.genre_var,
            values=genres,
            state="readonly",
            font=("Helvetica", 10)
        )
        self.genre_dropdown.pack(fill=tk.X, ipady=4)

        # -------------------------------
        # BUTTON (same row)
        # -------------------------------

        recommend_btn = tk.Button(
            control_panel,
            text="Recommend",
            command=self.show_movies,
            bg=self.accent_color,
            fg=self.bg_dark,
            activebackground="#00B3A6",
            activeforeground=self.bg_dark,
            font=("Helvetica", 10, "bold"),
            bd=0,
            cursor="hand2"
        )
        recommend_btn.grid(row=0, column=3, padx=20, pady=(18, 0), sticky="ew", ipady=6)

        # Bouton Surprise au milieu en bas du panneau
        random_btn = tk.Button(
            root,
            text="🎲 Surprise Me !",
            command=self.random_movie,
            bg="#A855F7",  # Violet vibrant pour l'effet "surprise"
            fg=self.fg_light,
            activebackground="#9333EA",
            activeforeground=self.fg_light,
            font=("Helvetica", 11, "bold"),
            bd=0,
            cursor="hand2"
        )
        random_btn.pack(pady=10, ipady=6, ipadx=20)

        # --- ZONE DE RÉSULTATS (DISPLAY) ---
        results_frame = tk.Frame(root, bg=self.bg_dark)
        results_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

        scrollbar = ttk.Scrollbar(results_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Utilisation d'un widget Text stylisé
        self.result_box = tk.Text(
            results_frame,
            height=20,
            width=80,
            font=("Helvetica", 11),
            bg=self.bg_card,
            fg=self.fg_light,
            bd=0,
            padx=20,
            pady=20,
            insertbackground=self.fg_light,
            yscrollcommand=scrollbar.set,
            wrap=tk.WORD
        )
        self.result_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.result_box.yview)

        # Configuration des "tags" pour formater dynamiquement le texte (Titres en surbrillance, etc.)
        self.result_box.tag_configure("title_style", font=("Helvetica", 14, "bold"), foreground=self.accent_color)
        self.result_box.tag_configure("synopsis_style", font=("Helvetica", 10), foreground=self.fg_muted)
        self.result_box.tag_configure("info_style", font=("Helvetica", 11, "italic"), foreground=self.fg_muted)


    # -------------------------------
    # LOGIQUE D'AFFICHAGE AMÉLIORÉE
    # -------------------------------
    def format_movie_display(self, movies, header_text=""):
        self.result_box.delete("1.0", tk.END)
        
        if header_text:
            self.result_box.insert(tk.END, header_text + "\n\n", "info_style")

        if not movies:
            self.result_box.insert(tk.END, "🍿 No movies found matching your criteria.", "info_style")
            return

        for movie in movies:
            # Gère les formats de retour différents selon tes fonctions SQL (2 ou 4 colonnes)
            if len(movie) == 4:
                _, title, genre, synopsis = movie
                title_line = f"{title.upper()}  |  {genre}\n"
            else:
                title, synopsis = movie
                title_line = f"{title.upper()}\n"

            # Insertion avec styles
            self.result_box.insert(tk.END, title_line, "title_style")
            self.result_box.insert(tk.END, f"{synopsis}\n", "synopsis_style")
            self.result_box.insert(tk.END, "─" * 60 + "\n\n", "synopsis_style") # Ligne séparatrice épurée

    def show_movies(self):
        genre = self.genre_var.get()
        if genre == "":
            self.result_box.delete("1.0", tk.END)
            self.result_box.insert(tk.END, "⚠️ Please select a genre first.", "info_style")
            return

        try:
            movies = database.get_movies_by_genre(genre)
            self.format_movie_display(movies, f"Showing recommendations for: {genre}")
        except Exception as e:
            self.result_box.insert(tk.END, f"Database Error: {e}")
    
    def search_movie(self):
        title = self.search_var.get().strip()
        if title == "":
            self.result_box.delete("1.0", tk.END)
            self.result_box.insert(tk.END, "⚠️ Please enter a movie title to search.", "info_style")
            return

        try:
            movies = database.search_movie_by_title(title)
            self.format_movie_display(movies, f"Search results for: '{title}'")
        except Exception as e:
            self.result_box.insert(tk.END, f"Error: {e}")
    
    def random_movie(self):
        try:
            movie = database.get_random_movie()
            if movie:
                self.format_movie_display([movie], "🎲 Your Random Surprise Pick:")
        except Exception as e:
            self.result_box.insert(tk.END, f"Error: {e}")


# -------------------------------
# MAIN PROGRAM
# -------------------------------

root = tk.Tk()
init_db()
app = MovieApp(root)
root.mainloop()
