-- Movie table
CREATE TABLE IF NOT EXISTS movies (
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    genre TEXT,
    synopsis TEXT
);

INSERT INTO movies (title, genre, synopsis) VALUES 
('The Dark Knight', 'Action', 'Batman faces the Joker to save Gotham City from chaos.'),
('Pulp Fiction', 'Crime', 'The lives of several Los Angeles criminals intertwine unexpectedly.'),
('Forrest Gump', 'Drama', 'The story of a simple man witnessing major events in American history.'),
('Matrix', 'Sci-Fi', 'A hacker discovers that his reality is only a computer simulation.'),
('The Lion King', 'Animation', 'A young lion must reclaim his place as king after his father''s death.'),
('Gladiator', 'Action', 'A fallen Roman general seeks revenge against a corrupt emperor.'),
('Seven', 'Thriller', 'Two detectives hunt a serial killer inspired by the seven deadly sins.'),
('Spirited Away', 'Animation', 'A young girl becomes trapped in a world inhabited by spirits.'),
('Fight Club', 'Drama', 'An insomniac office worker creates an underground fight club.'),
('Django Unchained', 'Western', 'A freed slave joins forces with a bounty hunter to rescue his wife.'),
('The Lord of the Rings', 'Fantasy', 'A hobbit embarks on a quest to destroy an evil ring and save Middle-earth.'),
('Shutter Island', 'Thriller', 'A marshal investigates the disappearance of a patient in a psychiatric hospital.'),
('Your Name', 'Animation', 'Two teenagers mysteriously swap bodies.'),
('The Grand Budapest Hotel', 'Comedy', 'The adventures of a hotel concierge and his protégé.'),
('Gone Girl', 'Thriller', 'A man becomes the prime suspect after his wife disappears.'),
('Blade Runner 2049', 'Sci-Fi', 'An officer uncovers a long-buried secret.'),
('Whiplash', 'Drama', 'A young drummer endures the pressure of a tyrannical teacher.'),
('Coco', 'Animation', 'A boy explores the world of the dead.'),
('The Revenant', 'Adventure', 'A trapper struggles to survive in the wilderness.'),
('Inglourious Basterds', 'War', 'A group of soldiers carries out violent missions during World War II.'),
('The Truman Show', 'Drama', 'A man discovers that his entire life is a television show.'),
('Joker', 'Drama', 'The descent of a man into madness.'),
('Mad Max: Fury Road', 'Action', 'A woman rebels in a post-apocalyptic world.'),
('Alien', 'Horror', 'A crew is hunted by a deadly extraterrestrial creature.'),
('Oldboy', 'Action', 'A man seeks revenge after being imprisoned for 15 years.'),
('Toy Story', 'Animation', 'Toys come to life when humans are not around.'),
('The Wolf of Wall Street', 'Biography', 'The rise and fall of a stockbroker.'),
('Green Book', 'Drama', 'A pianist and his driver travel across America.'),
('Arrival', 'Sci-Fi', 'A linguist attempts to communicate with aliens.'),
('1917', 'War', 'Two soldiers must deliver a critical message during World War I.');
