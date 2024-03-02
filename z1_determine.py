import sqlite3

def get_table_names(FridayProj5):
    try:
        # Connect to the database
        connection = sqlite3.connect(FridayProj5)
        cursor = connection.cursor()

        # Execute a query to get the table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        table_names = cursor.fetchall()

        # Print the table names
        print("Table Names:")
        for name in table_names:
            print(name[0])

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        if connection:
            connection.close()

# Replace 'your_database.db' with the path to your database file
database_path = 'FridayProj5.db'
get_table_names(database_path)
