import psycopg2

conn = psycopg2.connect(
  host = "localhost",
  dbname = "contacts_db",
  port = "5432",
  user = "postgres",
  password = "dammar"
)

cur = conn.cursor()

cur.execute("""
  CREATE TABLE IF NOT EXISTS contacts(
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  phone VARCHAR(100),
  email VARCHAR(100),
  city VARCHAR(100)
  );
""")
conn.commit()

cur.execute("""
Insert into contacts(name,phone,email,city) values('dammar bhatt','9805752792','dammarbhatt111@gmail.com','Mahendranagar'),('nirmala shahi','9805667780','nirmala@gmail.com','daijee'),('Chhabi Rana', '9800000003', 'chhabi@example.com', 'Dhangadhi'),('Deepa Karki', '9800000004', 'deepa@example.com', 'Biratnagar'),('Elina Joshi', '9800000005', 'elina@example.com', 'Nepalgunj')
""")
conn.commit()


print("Fetch all contact: ")
cur.execute("Select * from contacts;")

for row in cur.fetchall():
  print(row)


print("Search any contact using name: ")
searched_name = input("Enter name: ")
cur.execute("Select * from contacts where name ILIKE %s",('%' + searched_name +'%',))
for row in cur.fetchall():
  print(row)

print("deleting section: ")
delete_name  = input("enter name: ")
cur.execute("Delete from contacts where name = %s",(delete_name,))
conn.commit()
print(f"Delete {delete_name} records")

print("Contact after deletion: ")
cur.execute("Select * from contacts;")
for row in cur.fetchall():
  print(row)

cur.close()
conn.close()