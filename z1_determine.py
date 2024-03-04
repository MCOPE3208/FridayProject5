import sqlite3

def get_tables_and_columns(database_path):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Get table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    if tables:
        for table in tables:
            table_name = table[0]
            print(f"\nTable Name: {table_name}")

            # Get column names for each table
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()

            if columns:
                column_names = [column[1] for column in columns]
                print(f"Column Names: {', '.join(column_names)}")
            else:
                print(f"No columns found in the table {table_name}.")

    else:
        print("No tables found in the database.")

    connection.close()


database_path = 'FridayProj5.db'
get_tables_and_columns(database_path)
