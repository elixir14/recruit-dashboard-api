from flask_jwt_extended import JWTManager

from rest.flask_factory import app
from settings import env
from settings.env import JWT_SECRET_KEY
from utils.log import setup_logging

app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY  # Change this!
jwt = JWTManager(app)


def init():
    setup_logging(None, screen_log=True)


if __name__ == '__main__':
    init()
    app.run(host="0.0.0.0", port=env.SERVER_PORT, threaded=True)
