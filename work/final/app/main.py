#!venv/bin/python
'''Flask App'''

import os
from dotenv import load_dotenv
from flask import Flask
from flask_mysqldb import MySQL

load_dotenv()

app: Flask = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = os.getenv("MARIADB_ROOT_PASSWORD")
app.config['MYSQL_DB'] = 'data'

mysql: MySQL = MySQL(app)


@app.route("/")
def index() -> str:
    cursor = mysql.connection.cursor()
    cursor.execute("SHOW TABLES;")
    res = cursor.fetchall()
    tables = "\n".join(row[0] for row in res)
    return tables


if __name__ == "__main__":
    app.run(debug=True)
