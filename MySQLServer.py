#!/usr/bin/env python3
"""
MySQLServer.py
Creates the 'alx_book_store' database in a MySQL server.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"   # ← replace with your actual MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create the database if it does not already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Print error message if connection or creation fails
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Ensure proper cleanup of cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
