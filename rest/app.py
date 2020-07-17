from flask import Flask
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from rest.local_settings import DATABASE_URI, JWT_SECRET_KEY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY

jwt = JWTManager(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
