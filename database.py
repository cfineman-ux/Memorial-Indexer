import sqlite3

# create a connection object targeting a file named memorials.db
connection = None
cursor = None

# creating a table function
def createTable(cursor):
    TableName = """
    CREATE TABLE IF NOT EXISTS Profile (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        victim_name TEXT NOT NULL,
        birth_year INTEGER,
        address TEXT,
        latitude REAL,
        longitude REAL,
        biography TEXT
    )"""
    cursor.execute(TableName)

try:
    connection = sqlite3.connect("memorials.db")
    print("Database connected successfully.")

    # creates cursor object used to execute sql statements
    cursor = connection.cursor()

    # create table
    createTable(cursor)

except sqlite3.Error as error:
    print("Database error:", error)
finally:

    if cursor is not None:
        connection.commit()
        cursor.close()
        print("Table successfully created")

    if connection is not None:
        connection.close()
        print("Database connection is closed")
