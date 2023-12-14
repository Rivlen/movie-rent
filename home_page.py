import flask_login
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    if flask_login.current_user():
        return render_template('home_page.html')
    return render_template('home_page.html')
