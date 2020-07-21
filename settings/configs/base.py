from settings import env

DATABASE = {
    'name': env.DB_NAME,
    'user': env.DB_USER,
    'password': env.DB_PASSWORD,
    'server': env.DB_SERVER
}


class Config:
    SECRET_KEY = env.SECRET_KEY

    JWT_SECRET_KEY = env.JWT_SECRET_KEY

    DEBUG = False
