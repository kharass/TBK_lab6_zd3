import json
import psycopg2

from flask import Flask

app = Flask(__name__)

def getDatabase():
    return psycopg2.connect(database="postgres", user="postgres", password="postgres", host="172.17.0.2", port=7000)

@app.route('/cars', methods=['GET'])
def getCars():
    conn = getDatabase()
    cur = conn.cursor()
    cur.execute("SELECT * FROM cars")
    rows = cur.fetchall()
    conn.close()
    return json.dumps(rows)

@app.route('/cars/<int:year>', methods=['GET'])
def getCarsByYear(year):
    conn = getDatabase()
    cur = conn.cursor()
    cur.execute("SELECT * FROM cars WHERE year = %s", (year,))
    rows = cur.fetchall()
    conn.close()
    return json.dumps(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)