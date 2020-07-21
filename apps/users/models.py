from rest.app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    data = db.Column(db.String(500), nullable=True)

    def __init__(self, username, email, password, data):
        self.username = username
        self.email = email
        self.password = password
        self.data = data
