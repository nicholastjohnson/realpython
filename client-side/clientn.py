import sqlite3

with sqlite3.connect("movies.db") as connection:
	c = connection.cursor()

	# create a table
	c.execute("""CREATE TABLE upcoming_movies
					(title TEXT, year INT, rating TEXT,
					release TEXT, runtime INT, critics_review INT,
					audience_review INT)""")