-- Movie table
CREATE TABLE IF NOT EXISTS movies (
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    genre TEXT,
    synopsis TEXT
);

INSERT INTO movies (title, genre, synopsis) VALUES 
('The Dark Knight', 'Action', 'Batman affronte le Joker pour sauver Gotham City du chaos.'),
('Pulp Fiction', 'Crime', 'Les vies de plusieurs criminels de Los Angeles s''entremêlent de façon inattendue.'),
('Forrest Gump', 'Drama', 'L''histoire d''un homme simple qui traverse les grands événements des USA.'),
('Matrix', 'Sci-Fi', 'Un hacker découvre que sa réalité n''est qu''une simulation informatique.'),
('Le Roi Lion', 'Animation', 'Un jeune lion doit reprendre sa place de roi après la mort de son père.'),
('Gladiator', 'Action', 'Un général romain déchu cherche vengeance contre l''empereur corrompu.'),
('Seven', 'Thriller', 'Deux inspecteurs traquent un tueur en série qui s''inspire des sept péchés capitaux.'),
('Le Voyage de Chihiro', 'Animation', 'Une petite fille se retrouve piégée dans un monde peuplé d''esprits.'),
('Fight Club', 'Drama', 'Un employé de bureau insomniaque crée un club de combat clandestin.'),
('Django Unchained', 'Western', 'Un esclave libéré s''associe à un chasseur de primes pour sauver sa femme.'),
('Le Seigneur des Anneaux', 'Fantasy', 'Un hobbit part détruire un anneau maléfique pour sauver la Terre du Milieu.'),
('Shutter Island', 'Thriller', 'Un maréchal enquête sur la disparition d''une patiente dans un hôpital psychiatrique.'),
('Your Name', 'Animation', 'Deux adolescents échangent leurs corps de manière inexpliquée.'),
('The Grand Budapest Hotel', 'Comedy', 'Les aventures d''un concierge et de son protégé.'),
('Gone Girl', 'Thriller', 'Un homme devient suspect après la disparition de sa femme.'),
('Blade Runner 2049', 'Sci-Fi', 'Un officier découvre un secret enfoui.'),
('Whiplash', 'Drama', 'Un jeune batteur subit un professeur tyrannique.'),
('Coco', 'Animation', 'Un garçon explore le monde des morts.'),
('The Revenant', 'Adventure', 'Un trappeur lutte pour survivre.'),
('Inglourious Basterds', 'War', 'Un groupe de soldats mène des actions punitives.'),
('The Truman Show', 'Drama', 'Un homme découvre que sa vie est une émission.'),
('Joker', 'Drama', 'La descente d''un homme dans la folie.'),
('Mad Max: Fury Road', 'Action', 'Une femme se rebelle dans un monde post-apocalyptique.'),
('Alien', 'Horror', 'Un équipage est traqué par un extraterrestre.'),
('Oldboy', 'Action', 'Un homme cherche vengeance après 15 ans.'),
('Toy Story', 'Animation', 'Les jouets prennent vie.'),
('Le Loup de Wall Street', 'Biography', 'Ascension et chute d''un courtier.'),
('Green Book', 'Drama', 'Un pianiste et son chauffeur voyagent.'),
('Arrival', 'Sci-Fi', 'Une linguiste parle avec des aliens.'),
('1917', 'War', 'Deux soldats doivent livrer un message.');
