import tkinter as tk
from tkinter import ttk

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
            values=["Action", "Comedy", "Drama", "Horror", "Sci-Fi"] # will change with respect to the database later
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
    # TEMPORARY, WILL CHANGE WITH RESPECT TO THE DATABASE
    # -------------------------------
    def show_movies(self):
        genre = self.genre_var.get()

        # Clear previous results
        self.result_box.delete("1.0", tk.END)

        # Validation
        if genre == "":
            self.result_box.insert(tk.END, "Please select a genre first.")
            return

        self.result_box.insert(tk.END, f"Movies for {genre}:\n\n")

        # Dummy results (you replace later with DB)
        sample_movies = {
            "Action": ["John Wick", "Mad Max"],
            "Comedy": ["The Mask", "Superbad"],
            "Drama": ["The Pursuit of Happyness"],
            "Horror": ["The Conjuring"],
            "Sci-Fi": ["Interstellar", "Inception"]
        }

        movies = sample_movies.get(genre, [])

        for movie in movies:
            self.result_box.insert(tk.END, f"- {movie}\n")


# -------------------------------
# MAIN PROGRAM
# -------------------------------

root = tk.Tk()
app = MovieApp(root)
root.mainloop()
