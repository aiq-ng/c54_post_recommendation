import psycopg2
from psycopg2.extras import RealDictCursor  # For returning results as dictionaries
from dotenv import load_dotenv
import os

load_dotenv()

class Db_connection():
    def __init__(self):
        pass

    def get_db_connection(self):
        try:
            conn = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                cursor_factory=RealDictCursor  # Returns rows as dicts instead of tuples
            )
            return conn
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return None
        

    def database_connection(self):
        try:
            conn = self.Db_connection.get_db_connection()
        except Exception as e:
            return {"error": f"Database connection failed: {str(e)}"}
        
        return True
    

    def process_query_data(query, cursor):


        cursor.execute(query)

        rows = cursor.fetchall() 

        rows = [dict(row) for row in rows]

        return rows
    
    

