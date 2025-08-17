# MySQLServer.py
import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL Server (adjust host, user, password to your setup)
        connection = mysql.connector.connect(
            host="localhost",        # or "127.0.0.1"
            user="root",             # change to your MySQL username
            password="your_password" # change to your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create DB safely (no error if it already exists)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection safely
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()