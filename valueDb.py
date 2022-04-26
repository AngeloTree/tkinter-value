from sqlite3 import dbapi2
import psycopg2
import psycopg2.extras
import valueGui
from requests import delete

DB_HOST = "localhost"
DB_NAME = "sandbox"
DB_USER = "angelo"
DB_PASS = "abc123"

def get_connection():
   conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
   return conn

def update_number(newNum):
    with get_connection() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            # cursor.execute(f"SELECT * FROM number WHERE id = {1}")
            # print(cursor.fetchone()['num'])
            cursor.execute(f"UPDATE number SET num = {newNum} WHERE id = 4")
            print("Value updated.")
    

