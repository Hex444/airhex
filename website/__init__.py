from flask import Flask, render_template
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


def create_database(app):
    if not path.exists('website/' + 'database.db'):
        db.create_all(app=app)
        print('Created Database')

# Initialization

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
app.config["SECRET_KEY"] = "3a2e90fb987dd93743b5e35d"

db = SQLAlchemy(app)

from .models import User
create_database(app)

bcrypt = Bcrypt(app)
loginmanager = LoginManager(app)
loginmanager.login_view = 'auth.login'

@loginmanager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from .views import views
from .auth import auth
app.register_blueprint(views)
app.register_blueprint(auth)