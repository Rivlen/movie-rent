from flask import Flask, request, render_template, redirect
import flask_login
from secret_key import secret_key
from user import User

app = Flask(__name__)
app.secret_key = secret_key

login_manager = flask_login.LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
