from flask import render_template

from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'} #Mock user (to not worry about it for now)
    return render_template('index.html', title='Home', user=user)