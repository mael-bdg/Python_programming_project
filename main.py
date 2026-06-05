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
        
        self.bg_dark = "#141A29"       # background principal (Dark Navy)
        self.bg_card = "#1F293D"       # background of cards and panels (Darker Slate)
        self.fg_light = "#FFFFFF"      # Primary text color (White)
        self.fg_muted = "#9CA3AF"      # secondary text color (Muted Gray)
        self.accent_color = "#00D2C4"  # Accent color for highlights and buttons (Bright Cyan)
        self.btn_bg = "#2563EB"        # Button background (Vibrant Blue)

        self.root.configure(bg=self.bg_dark)

        # Configuration of ttk styles for Combobox
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TCombobox", fieldbackground=self.bg_card, background=self.bg_card, foreground=self.fg_light)
        
        # --- HEADER ---
        header_frame = tk.Frame(root, bg=self.bg_dark)
        header_frame.pack(fill=tk.X, padx=30, pady=20)

        # -------------------------------
        # TITLE
        # -------------------------------
        title = tk.Label(
            header_frame, 
            text="🎬 CineReco", 
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

        add_movie_btn = tk.Button(
            header_frame,
            text="+ Add Movie",
            command=self.open_add_movie_window,
            bg=self.accent_color,
            fg=self.bg_dark,
            activebackground="#00B3A6",
            activeforeground=self.bg_dark,
            font=("Helvetica", 10, "bold"),
            bd=0,
            cursor="hand2",
            padx=15,
            pady=5
        )
        add_movie_btn.pack(side=tk.RIGHT, pady=5)

        # --- SIDEBAR / TOP BAR MIX ---
        control_panel = tk.Frame(root, bg=self.bg_card, bd=0, highlightthickness=0)
        control_panel.pack(fill=tk.X, padx=30, pady=10, ipady=15)

        # Internal grid configuration for better spacing
        control_panel.columnconfigure((0, 1, 2, 3), weight=1)

        # Section Search by Title
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

        # Section Filter by Genre
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

        # Surprise Me Button (Random Movie)
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

        # --- DISPLAY ---
        results_frame = tk.Frame(root, bg=self.bg_dark)
        results_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

        scrollbar = ttk.Scrollbar(results_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Use a Text widget for better formatting capabilities (titles, synopses, comments)
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

        # Configuration of text tags for styling different parts of the movie display
        self.result_box.tag_configure("title_style", font=("Helvetica", 14, "bold"), foreground=self.accent_color)
        self.result_box.tag_configure("synopsis_style", font=("Helvetica", 10), foreground=self.fg_muted)
        self.result_box.tag_configure("info_style", font=("Helvetica", 11, "italic"), foreground=self.fg_muted)


    # -------------------------------
    # FUNCTIONS FOR DISPLAY AND INTERACTIONS
    # -------------------------------
    def format_movie_display(self, movies, header_text=""):
        self.result_box.delete("1.0", tk.END)
        
        if header_text:
            self.result_box.insert(tk.END, header_text + "\n\n", "info_style")

        if not movies:
            self.result_box.insert(tk.END, "🍿 No movies found matching your criteria.", "info_style")
            return

        for movie in movies:
            # S'adapte au nombre de colonnes retournées
            if len(movie) == 4:
                title, synopsis, director, comment = movie
            elif len(movie) == 6:
                _, title, _, synopsis, director, comment = movie
            else:
                title, synopsis = movie[0], movie[1]
                director, comment = "Unknown", ""

            # structured display with styling
            title_line = f"🎬 {title.upper()}"
            if director:
                title_line += f"  (Directed by: {director})"
            title_line += "\n"

            self.result_box.insert(tk.END, title_line, "title_style")
            self.result_box.insert(tk.END, f"Synopsis:\n{synopsis}\n", "synopsis_style")
            
            if comment:
                self.result_box.insert(tk.END, f"My Review:\n💬 {comment}\n", "info_style")
                
            self.result_box.insert(tk.END, "─" * 60 + "\n\n", "synopsis_style")

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

    
    def open_add_movie_window(self):
        # Create a new Toplevel window for adding a movie
        add_win = tk.Toplevel(self.root)
        add_win.title("Add New Movie")
        add_win.geometry("450x550")
        add_win.configure(bg=self.bg_dark)
        add_win.grab_set() # Block interaction with the main window until this one is closed

        # Style dictionaries for consistent styling
        lbl_style = {"bg": self.bg_dark, "fg": self.fg_light, "font": ("Helvetica", 10, "bold"), "anchor": "w"}
        entry_style = {"bg": self.bg_card, "fg": self.fg_light, "bd": 0, "highlightthickness": 1, "highlightbackground": "#374151", "highlightcolor": self.accent_color, "insertbackground": self.fg_light, "font": ("Helvetica", 11)}

        # Header
        tk.Label(add_win, text="🎬 ADD A NEW MOVIE", font=("Helvetica", 14, "bold"), bg=self.bg_dark, fg=self.accent_color).pack(pady=15)

        # Title
        tk.Label(add_win, text="Title *", **lbl_style).pack(fill=tk.X, padx=30, pady=(5, 2))
        title_entry = tk.Entry(add_win, **entry_style)
        title_entry.pack(fill=tk.X, padx=30, ipady=4)

        # Director
        tk.Label(add_win, text="Director", **lbl_style).pack(fill=tk.X, padx=30, pady=(10, 2))
        director_entry = tk.Entry(add_win, **entry_style)
        director_entry.pack(fill=tk.X, padx=30, ipady=4)

        # Genre
        tk.Label(add_win, text="Genre *", **lbl_style).pack(fill=tk.X, padx=30, pady=(10, 2))
        genre_entry = tk.Entry(add_win, **entry_style)
        genre_entry.pack(fill=tk.X, padx=30, ipady=4)

        # Synopsis
        tk.Label(add_win, text="Synopsis *", **lbl_style).pack(fill=tk.X, padx=30, pady=(10, 2))
        synopsis_text = tk.Text(add_win, height=4, bg=self.bg_card, fg=self.fg_light, bd=0, highlightthickness=1, highlightbackground="#374151", highlightcolor=self.accent_color, insertbackground=self.fg_light, font=("Helvetica", 10), wrap=tk.WORD)
        synopsis_text.pack(fill=tk.X, padx=30)

        # Comment
        tk.Label(add_win, text="Your Comment / Review", **lbl_style).pack(fill=tk.X, padx=30, pady=(10, 2))
        comment_text = tk.Text(add_win, height=3, bg=self.bg_card, fg=self.fg_light, bd=0, highlightthickness=1, highlightbackground="#374151", highlightcolor=self.accent_color, insertbackground=self.fg_light, font=("Helvetica", 10), wrap=tk.WORD)
        comment_text.pack(fill=tk.X, padx=30)

        # Internal function to handle saving the movie to the database
        def save_movie():
            t = title_entry.get().strip()
            g = genre_entry.get().strip()
            d = director_entry.get().strip()
            s = synopsis_text.get("1.0", tk.END).strip()
            c = comment_text.get("1.0", tk.END).strip()

            if not t or not g or not s:
                tk.Label(add_win, text="⚠️ Title, Genre and Synopsis are required!", bg=self.bg_dark, fg="#EF4444", font=("Helvetica", 9, "bold")).pack(pady=5)
                return

            try:
                database.insert_movie(t, g, s, d, c)
                # Refresh the genres in the main dropdown
                self.genre_dropdown['values'] = database.get_all_genres()
                add_win.destroy() # Close the window

                # Temporary success message in the console or box
                self.result_box.delete("1.0", tk.END)
                self.result_box.insert(tk.END, f"✅ '{t}' successfully added to the database!", "info_style")
            except Exception as e:
                print(f"Error saving movie: {e}")

        # Save Button
        tk.Button(add_win, text="Save Movie", command=save_movie, bg=self.btn_bg, fg=self.fg_light, font=("Helvetica", 11, "bold"), bd=0, cursor="hand2").pack(fill=tk.X, padx=30, pady=25, ipady=6)


# -------------------------------
# MAIN PROGRAM
# -------------------------------

root = tk.Tk()
init_db()
app = MovieApp(root)
root.mainloop()
