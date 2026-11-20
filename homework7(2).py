import sqlite3
conn = sqlite3.connect("cinema.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS movies"(id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,genre TEXT,year INTEGER)""")
def create_movie(title,genre,year):
        .execute("INSERT INTO movies (title, genre, year) VALUES (?, ?, ?)", (title, genre, year))
        conn.commit()

def read_movies():
        c.execute("SELECT * FROM movies")
        movies = c.fetchall()
        for movie in movies:
            movie=c.fetchall()
            for movie in movie:
                print(movie)


def update_movie(id, year):
        c.execute("UPDATE movies SET year = ? WHERE id = ?", (year, id))
        conn.commit()

def delete_movie(id):

        c.execute("DELETE FROM movies WHERE id = ?", (id,))
        conn.commit()
create_movie("Интерстеллар", "Фантастика", 2014)
create_movie("Начало", "Боевик", 2010)
read_movies()
update_movie(1, 2024)
delete_movie(2)
read_movies()
conn.close()