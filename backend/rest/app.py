

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

app = Flask(__name__)

from local_settings import (db_username,db_password,DATABASE_URI,SQLALCHEMY_TRACK_MODIFICATIONS)

jwt = JWTManager(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)


