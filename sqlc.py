# executemany() method
import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

# insert multiple records using a tuple
	cities = [
		('New York City', 'Northeast'),
 ('San Francisco', 'West'),
 ('Chicago', 'Midwest'),
 ('Houston', 'South'),
 ('Phoenix', 'West'),
 ('Boston', 'Northeast'),
 ('Los Angeles', 'West'),
 ('Houston', 'South'),
 ('Philadelphia', 'Northeast'),
 ('San Antonio', 'South'),
 ('San Diego', 'West'),
('Dallas', 'South'),
 ('San Jose', 'West'),
 ('Jacksonville', 'South'),
 ('Indianapolis', 'Midwest'),
 ('Austin', 'South'),
 ('Detroit', 'Midwest')
		 ]

# insert data into table
	c.executemany('INSERT INTO regions VALUES(?, ?)', cities)
	c.execute("SELECT * FROM regions ORDER BY region ASC")

	rows = c.fetchall()

	for r in rows:
		print r[0], r[1]