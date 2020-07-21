from settings.configs.base import DATABASE, Config

DB_URI = "postgresql://{user}:{password}@{server}/{name}".format(**DATABASE)


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    SQLALCHEMY_DATABASE_URI = DB_URI
