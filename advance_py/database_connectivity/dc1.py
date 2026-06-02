import psycopg2
for dotenv import load_dotenv
import os

load.dotenv()
# load env file 

def get_connection():
  conn = psycopg2.connect(
    host = os.getenv("DB_HOST"),
    port = os.getenv("DB_PORT"),
    dbname = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
  )

try:
  conn = get_connection()
  print("Connected sucessfully!")
  conn.close()
except Exception as e:
  print("Connection problem: ",e)