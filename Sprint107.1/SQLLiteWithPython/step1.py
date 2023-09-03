import sqlalchemy

# Create an engine that connects to a SQLite database file named "example.sqlite3"
engine = sqlalchemy.create_engine('sqlite:///Data/textbook.sqlite3')

with engine.connect() as connection:
  # Run an SQL query
  # results = connection.execute("""SELECT * FROM arabic""")
  # rows = results.fetchall()

  sql_query = sqlalchemy.text("SELECT * FROM simple_books")  # Execute the query
  results = connection.execute(sql_query)
  rows = results.fetchall()

  # Print results
  for row in rows:
      print(row)