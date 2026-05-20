CREATE DATABASE IF NOT EXISTS brouillon;
USE brouillon;

-- Movie table
CREATE TABLE Movie (
	movie_id int primary key auto_increment,
    title varchar(150),
    genre varchar(50),
    synopsis varchar(1000)
);

INSERT INTO Movie (title, genre, synopsis) VALUES 
('The Dark Knight', 'Action', 'Batman affronte le Joker pour sauver Gotham City du chaos.'),
('Pulp Fiction', 'Crime', 'Les vies de plusieurs criminels de Los Angeles s''entremêlent de façon inattendue.'),
('Forrest Gump', 'Drame', 'L''histoire d''un homme simple qui traverse les grands événements des USA.'),
('Matrix', 'Science-Fiction', 'Un hacker découvre que sa réalité n''est qu''une simulation informatique.'),
('Le Roi Lion', 'Animation', 'Un jeune lion doit reprendre sa place de roi après la mort de son père.'),
('Gladiator', 'Action', 'Un général romain déchu cherche vengeance contre l''empereur corrompu.'),
('Seven', 'Thriller', 'Deux inspecteurs traquent un tueur en série qui s''inspire des sept péchés capitaux.'),
('Le Voyage de Chihiro', 'Animation', 'Une petite fille se retrouve piégée dans un monde peuplé d''esprits.'),
('Fight Club', 'Drame', 'Un employé de bureau insomniaque crée un club de combat clandestin.'),
('Django Unchained', 'Western', 'Un esclave libéré s''associe à un chasseur de primes pour sauver sa femme.'),
('Le Seigneur des Anneaux', 'Fantastique', 'Un hobbit part détruire un anneau maléfique pour sauver la Terre du Milieu.'),
('Shutter Island', 'Thriller', 'Un maréchal enquête sur la disparition d''une patiente dans un hôpital psychiatrique.'),
('Your Name', 'Animation', 'Deux adolescents que tout oppose échangent leurs corps de manière inexpliquée.'),
('The Grand Budapest Hotel', 'Comédie', 'Les aventures d''un concierge d''hôtel légendaire et de son jeune protégé.'),
('Gone Girl', 'Thriller', 'Un homme devient le suspect numéro un après la disparition de sa femme.'),
('Blade Runner 2049', 'Science-Fiction', 'Un nouvel officier découvre un secret enfoui qui menace le reste de la société.'),
('Whiplash', 'Drame', 'Un jeune batteur de jazz intègre un conservatoire de haut niveau sous un prof tyrannique.'),
('Coco', 'Animation', 'Un jeune garçon voyage au pays des morts pour découvrir l''histoire de sa famille.'),
('The Revenant', 'Aventure', 'Un trappeur lutte pour sa survie après avoir été laissé pour mort en forêt.'),
('Inglourious Basterds', 'Guerre', 'Un groupe de soldats juifs mène des actions punitives dans la France occupée.'),
('The Truman Show', 'Comédie dramatique', 'Un homme découvre que sa vie entière est une émission de télé-réalité.'),
('Joker', 'Drame', 'L''ascension d''un comédien raté vers une folie meurtrière à Gotham.'),
('Mad Max: Fury Road', 'Action', 'Une femme se rebelle contre un tyran dans un futur post-apocalyptique.'),
('Alien', 'Horreur', 'L''équipage d''un vaisseau spatial est traqué par une créature extraterrestre.'),
('Oldboy', 'Action', 'Un homme séquestré pendant 15 ans cherche à comprendre pourquoi.'),
('Toy Story', 'Animation', 'Les jouets d''un petit garçon prennent vie dès qu''il quitte sa chambre.'),
('Le Loup de Wall Street', 'Biopic', 'L''ascension et la chute d''un courtier en bourse aux pratiques excessives.'),
('Green Book', 'Drame', 'Un pianiste noir et son chauffeur blanc font une tournée dans le sud des USA.'),
('Arrival', 'Science-Fiction', 'Une linguiste tente de communiquer avec des extraterrestres fraîchement débarqués.'),
('1917', 'Guerre', 'Deux soldats britanniques doivent délivrer un message vital en territoire ennemi.');

select * from Movie;

