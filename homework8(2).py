import sqlite3

db = sqlite3.connect("movies.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    genre TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
)
""")

cursor.execute("""
INSERT INTO users (name) VALUES 
('Anna'), ('Bob'), ('Vlad'), ('Gleb'), ('Dasha')
""")

cursor.execute("""
INSERT INTO movies (title, genre) VALUES 
('Иди и смотри', 'ужас'),
('Изгнание дьявола', 'ужас'),
('Зеркала', 'ужас'),
('Оно', 'ужас'),
('Заклятие', 'ужас')
""")

cursor.execute("""
INSERT INTO reviews (user_id, movie_id, rating) VALUES 
(1, 1, 9),
(2, 1, 8),
(3, 2, 10),
(4, 2, 7),
(5, 3, 9),
(1, 3, 6),
(2, 4, 8),
(3, 4, 9),
(4, 1, 10),
(5, 2, 8)
""")

db.commit()

cursor.execute("""
SELECT users.name, movies.title, reviews.rating
FROM reviews
JOIN users ON reviews.user_id = users.id
JOIN movies ON reviews.movie_id = movies.id
""")
print("Отзывы пользователей:", cursor.fetchall())

cursor.execute("""
SELECT movies.title, reviews.rating
FROM movies
LEFT JOIN reviews ON movies.id = reviews.movie_id
""")
print("Все фильмы:", cursor.fetchall())

cursor.execute("""
SELECT AVG(rating), MAX(rating), MIN(rating)
FROM reviews
""")
print("Средняя, макс. и мин. оценки:", cursor.fetchall())

db.close()






