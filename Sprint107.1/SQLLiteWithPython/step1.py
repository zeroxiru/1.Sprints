import sqlalchemy
from sqlalchemy import text

# Create an engine that connects to a SQLite database file named "example.sqlite3"
engine = sqlalchemy.create_engine('sqlite:///textbook.sqlite3')

with engine.connect() as connection:
  # Run an SQL query
  results = connection.execute("SELECT * FROM books")
  rows = results.fetchall()

  # Print results
  for row in rows:
      print(row)