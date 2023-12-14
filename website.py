from flask import Flask, request, render_template, redirect
from flask_login import LoginManager
from secret_key import secret_key
from user import User

app = Flask(__name__)
app.secret_key = secret_key

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(conn, cursor, user_id):
    return User.get(conn, cursor, user_id)
