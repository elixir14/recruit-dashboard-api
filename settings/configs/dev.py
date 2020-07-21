from settings.configs.base import Config, DATABASE

DB_URI = "postgresql://{user}:{password}@{server}/{name}".format(**DATABASE)


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = "Dummy String"
