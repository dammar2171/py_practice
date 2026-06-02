import psycopg2

conn = psycopg2.connect(
  host = "localhost",
  user = "postgres"
  dbname = "todo_db"
  port = "5432",
  password = "dammar",
)

cur = conn.cursor()

cur.execute(
  """
  CREATE TABLE todo(
  id SERIAL PRIMARY KEY ,
  title VARCHAR(100),
  status VARCHAR(100) DEFAULT "pending",
  created_at TIMESTAMP DEFAULT NOW()
"""
)
conn.commit()

cur.execute("""INSERT INTO contacts (title,status) VALAUES ("reading books","pending"),("zymming","completed"),("coding","completed"),("writing","pending"),("running","completed")
""")
conn.commit()

status = "pending"
cur.execute("SELECT * FROM todo where status =%s",(status))
for row in cur.fetchall():
  print(row)

