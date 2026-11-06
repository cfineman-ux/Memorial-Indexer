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

# function for adding sample data for testing purposes
def insertSampleData(cursor, connection):
    values = [
        ("Rosa Levi",1892,"Rosenthaler Str. 39, 10178 Berlin, Germany",
        52.5251, 13.4028, "osa Levi lived at Rosenthaler Straß" ),
        ("Otto Hirsch",1890,"Poststraße 4, 10178 Berlin, Germany",
        52.5170,13.4070,"Otto Hirsch was a lawyer an"),
        ("Hanna Stern",1921,"Oranienburger Str. 28, 10117 Berlin, Germany",
        52.5242, 13.3946,"Hanna Stern was a student")
    ]

    # check if table is empty 
    count = """SELECT COUNT(*) FROM Profile"""
    cursor.execute(count)
    result = list(cursor.fetchone())
    
    if result[0] == 0:
        # execute sql statement
        sql_query = "INSERT INTO Profile (victim_name, birth_year, address,latitude,longitude,biography) VALUES(?,?,?,?,?,?)"
        cursor.executemany(sql_query, values)
    else:
        print("not adding more data")
    
    # save the insertion to disk
    connection.commit()

    # display the data
    display_table = """SELECT * FROM Profile"""
    cursor.execute(display_table)

    for row in cursor.fetchall():
        print(row)
    
try:
    connection = sqlite3.connect("memorials.db")
    print("Database connected successfully.")

    cursor = connection.cursor()

    # create table and insert data
    createTable(cursor)
    insertSampleData(cursor, connection)

except sqlite3.Error as error:
    print("Database error:", error)
finally:

    if cursor is not None:
        cursor.close()

    if connection is not None:
        connection.close()
        print("Database connection is closed")
