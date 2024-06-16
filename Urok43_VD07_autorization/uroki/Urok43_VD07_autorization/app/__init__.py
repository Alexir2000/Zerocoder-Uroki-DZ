from flask import Flask
# ищем как flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# ищем как flask-bcrypt
from flask_bcrypt import Bcrypt
# ищем как flask-login
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from uroki.Urok43_VD07_autorization.app import routes
