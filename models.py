# models.py
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    api_key = db.Column(db.String(64), unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)
        self.api_key = 'uk_test_123456789'

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'api_key': self.api_key
        }