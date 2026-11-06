import sqlite3

# TODO: create a connection object targeting a file named memorials.db
connection = None
cursor = None

try:
    connection = sqlite3.connect("file:memrials.db?mode=rw", uri = True)
    print("Database connected successfully.")

    cursor = connection.cursor()
except sqlite3.Error as error:
    print("Database error:", error)
finally:

    if cursor is not None:
        cursor.close()

    if connection is not None:
        connection.close()
        print("Database connection is closed")
