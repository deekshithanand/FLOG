from flask import Flask, render_template, request, session, redirect, flash,url_for
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os
from utils import validateForm

app = Flask(__name__)


db = json.load(open('db.json'))
app.config['MYSQL_PASSWORD'] = db['password']
app.config['MYSQL_USER'] = db['user']
app.config['MYSQL_DB'] = db['db']
app.config['MYSQL_HOST'] = db['host']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

app.secret_key = os.urandom(24)


@app.route('/')
def index():
   
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/blogs/<int:id>/')
def blogs(id):
    return render_template('blogs.html', blog_id=id)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        formData = request.form
        status,message = validateForm(formData)
        if(status == True):
            flash(message,'danger')
            return redirect(url_for('register'))
        
        return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/write-blog/', methods=['GET', 'POST'])
def write_blog():
    return render_template('write-blog.html')


@app.route('/my-blogs/')
def my_blog():
    return render_template('my-blog.html')


@app.route('/edit-blog/<int:id>', methods=['GET', 'POST'])
def edit_blog(id):
    return render_template('edit-blog.html')


@app.route('/delete-blog/<int:id>', methods=['POST'])
def delete_blog():
    return 'success'


@app.route('/logout/')
def logout():
    return render_template('logout.html')


if __name__ == '__main__':
    app.run(debug=True)
