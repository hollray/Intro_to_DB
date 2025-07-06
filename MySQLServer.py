import mysql.connector
from mysql.connector import Error


def create_database():
    # --- Configuration: for my MySQL Server ---
    db_config = {
        'host': 'localhost',  '
        'user': 'root',  
        'password': 'Password@1234', 
        'port': 3306  
    }
    
    connection = None
    cursor = None

    try:
        # This establishes the connection to the MySQL server (without specifying a database initially)
        connection = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            port=db_config['port']
        )

        if connection.is_connected():
            print(
                f"Successfully connected to MySQL Server version {connection.get_server_info()}")
            cursor = connection.cursor()

            # SQL query to create the database if it doesn't exist
            # Using IF NOT EXISTS ensures the script doesn't fail if the DB exists
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

            cursor.execute(create_db_query)
            print(f"Database 'alx_book_store' created successfully!")
        else:
            print("Failed to connect to MySQL Server.")

    except Error as e:
        # Handle specific connection errors
        if e.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif e.errno == mysql.connector.errorcode.CR_CONN_HOST_ERROR:
            print("Error: Cannot connect to MySQL host. Check the host and port.")
        else:
            print(f"Error: Failed to connect to DB or create database. {e}")

    finally:
        # Close the cursor and connection if they were opened
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")


if __name__ == "__main__":
    create_database()
