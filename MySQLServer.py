import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (replace with your actual MySQL password)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error: Unable to connect or create database.\nDetails: {e}")

    finally:
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
        except:
            pass

if __name__ == "__main__":
    create_database()
