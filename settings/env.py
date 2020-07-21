import os

from dotenv import load_dotenv

load_dotenv()

APP_MODE = os.getenv('APP_MODE', 'dev')

SERVER_PORT = os.getenv('SERVER_PORT')

SECRET_KEY = os.getenv('SECRET_KEY')
DB_SERVER = os.getenv('DB_SERVER')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
