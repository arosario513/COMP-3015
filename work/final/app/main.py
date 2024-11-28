#!venv/bin/python3
'''Flask App'''

import os
import re
from flask_login import LoginManager, login_required, current_user, UserMixin, login_user, logout_user
from flask import Flask, render_template, redirect, url_for, request, flash, session
from dotenv import load_dotenv
from flask_mysqldb import MySQL
import MySQLdb.cursors
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

load_dotenv()

app: Flask = Flask(__name__)
app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST", "db")
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = os.getenv("MARIADB_ROOT_PASSWORD")
app.config['MYSQL_DB'] = 'data'
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

mysql: MySQL = MySQL(app)
ph: PasswordHasher = PasswordHasher()


login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Please log in to access this page."
login_manager.login_message_category = "info"


class User(UserMixin):
    '''
    User Class
    Attributes:
        id: int
        name: str
        email: str
    '''

    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email


@login_manager.user_loader
def load_user(user_id):
    '''Load User'''
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
    account = cursor.fetchone()
    if account:
        return User(id=account['id'], name=account['name'], email=account['email'])
    return None


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and all(field in request.form for field in ['name', 'email', 'password']):
        name = request.form['name']
        email = request.form['email']
        password = ph.hash(request.form['password'])
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        account = cursor.fetchone()
        if account:
            flash('Email is already registered!', 'danger')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address!', 'warning')
        elif not name or not password or not email:
            flash('Please fill out the form!', 'warning')
        else:
            cursor.execute(
                'INSERT INTO users (name, email, password) VALUES (%s, %s, %s)', (name, email, password))
            mysql.connection.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        account = cursor.fetchone()

        if account:
            try:
                if ph.verify(account['password'], password):
                    user = User(
                        id=account['id'], name=account['name'], email=account['email'])
                    login_user(user)
                    session['loggedin'] = True
                    session['id'] = account['id']
                    session['name'] = account['name']
                    flash('Logged in successfully!', 'success')
                    return redirect(url_for('dashboard'))
                flash('Invalid email or password.', 'danger')
            except VerifyMismatchError:
                flash('Invalid email or password.', 'danger')
        else:
            flash('Invalid email or password.', 'danger')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    '''Logs out of session'''
    logout_user()
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM projects WHERE user_id = %s',
                   (current_user.id,))
    projects = cursor.fetchall()
    return render_template('dashboard.html', name=current_user.name, projects=projects)


@app.route('/project/create', methods=['GET', 'POST'])
@login_required
def create_project():
    if request.method == 'POST' and all(field in request.form for field in ['title', 'description', 'date_start']):
        title = request.form['title']
        description = request.form['description']
        date_start = request.form['date_start']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO projects (user_id, title, description, date_start) VALUES (%s, %s, %s, %s)',
                       (current_user.id, title, description, date_start))
        mysql.connection.commit()
        flash('Project created successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('create_project.html')


@app.route('/project/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_project(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST' and all(field in request.form for field in ['title', 'description', 'date_start']):
        title = request.form['title']
        description = request.form['description']
        date_start = request.form['date_start']
        is_finished = 'is_finished' in request.form
        cursor.execute('UPDATE projects SET title=%s, description=%s, date_start=%s, is_finished=%s WHERE id=%s AND user_id=%s',
                       (title, description, date_start, is_finished, id, current_user.id))
        mysql.connection.commit()
        flash('Project updated successfully!', 'success')
        return redirect(url_for('dashboard'))
    cursor.execute(
        'SELECT * FROM projects WHERE id = %s AND user_id = %s', (id, current_user.id))
    project = cursor.fetchone()
    return render_template('edit_project.html', project=project)


@app.route('/project/delete/<int:id>', methods=['POST'])
@login_required
def delete_project(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM tasks WHERE project_id = %s', (id,))
    tasks = cursor.fetchall()
    if tasks:
        flash('Cannot delete project with assigned tasks.', 'warning')
    else:
        cursor.execute(
            'DELETE FROM projects WHERE id = %s AND user_id = %s', (id, current_user.id))
        mysql.connection.commit()
        flash('Project deleted successfully.', 'success')
    return redirect(url_for('dashboard'))


@app.route('/project/<int:project_id>/tasks')
@login_required
def list_tasks(project_id):
    session['current_project'] = project_id
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM tasks WHERE project_id = %s', (project_id,))
    tasks = cursor.fetchall()
    return render_template('list_tasks.html', project_id=project_id, tasks=tasks)


@app.route('/project/<int:project_id>/task/create', methods=['GET', 'POST'])
def create_task(project_id):
    if request.method == 'POST':
        task_description = request.form['description']
        task_date = request.form['date']
        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO tasks (project_id, description, date) VALUES (%s, %s, %s)',
            (project_id, task_description, task_date)
        )
        mysql.connection.commit()
        return redirect(url_for('list_tasks', project_id=project_id))
    return render_template('create_task.html', project_id=project_id)


@app.route('/task/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_task(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        description = request.form['description']
        date = request.form['date']
        completed = 'completed' in request.form
        cursor.execute(
            'UPDATE tasks SET description = %s, date = %s, completed = %s WHERE id = %s',
            (description, date, completed, id)
        )
        mysql.connection.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('list_tasks', project_id=session.get('current_project')))
    cursor.execute('SELECT * FROM tasks WHERE id = %s', (id,))
    task = cursor.fetchone()
    return render_template('edit_task.html', task=task)


@app.route('/task/delete/<int:id>', methods=['POST'])
@login_required
def delete_task(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('DELETE FROM tasks WHERE id = %s', (id,))
    mysql.connection.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('list_tasks', project_id=session.get('current_project')))


if __name__ == '__main__':
    app.run(debug=True)
