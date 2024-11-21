#!venv/bin/python3
'''Flask App'''

import os
import re
from dotenv import load_dotenv
from flask_mysqldb import MySQL, MySQLdb
from flask import Flask, render_template, redirect, url_for, request, session

load_dotenv()

app: Flask = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = os.getenv("MARIADB_ROOT_PASSWORD")
app.config['MYSQL_DB'] = 'data'

mysql: MySQL = MySQL(app)


@app.route("/register", methods=["GET", "POST"])
def register():
    '''Register Function'''
    msg = ''

    if request.method == 'POST' and 'nombre' in request.form and 'email' in request.form and 'password' in request.form:
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        account = cursor.fetchone()
        if account:
            msg = 'Email is already registered'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):

            msg = 'Invalid email'
        elif not nombre or not password or not email:
            msg = 'Fill the form'
        else:
            cursor.execute(
                'INSERT INTO usuarios (name, email, password) VALUES (%s, %s, %s)', (nombre, email, password,))
            mysql.connection.commit()
            msg = 'Registered successfully'
            return redirect(url_for('login'))
    if request.method == 'POST':
        msg = 'Por favor llena el formulario!'
    return render_template('register.html', msg=msg)


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''Login Function'''
    msg = ''

    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM usuarios WHERE email = %s AND password = %s', (email, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['nombre'] = account['nombre']
            return redirect(url_for('dashboard'))
    else:
        msg = 'Invalid Login'
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    '''Logout Function'''
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('nombre', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
