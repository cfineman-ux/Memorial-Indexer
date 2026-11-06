from flask import Flask, jsonify
import sqlite3


app = Flask(__name__)

@app.route("/")
def index():
    return "Memorial Indexer API is running!"

# route for data
@app.route("/api/stones")
def info():
    connection = None
    try:
        connection = sqlite3.connect("memorials.db")
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM Profile""")
        rows = cursor.fetchall()
        infoDict = [dict(row) for row in rows]
        print(infoDict)

    except sqlite3.Error as error:
        return jsonify({"error": "Database error"}), 500
    else:
        return jsonify(infoDict), 200
    finally:
        if connection is not None:
            connection.close()
  

if __name__ == "__main__":
    app.run(debug=True)
    

    