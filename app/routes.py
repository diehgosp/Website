from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/generic')
def generic():
    return render_template('generic.html', title='Generic')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
