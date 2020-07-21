from flask import Flask
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from settings.configs import config
from settings.env import APP_MODE

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config[APP_MODE])
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)

    return app
