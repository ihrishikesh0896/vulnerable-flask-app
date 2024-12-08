# app.py
from flask import Flask, jsonify, render_template
from config import Config
from models import db, User
import os
import stripe
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Hardcoded API keys (intentionally insecure for testing)
STRIPE_KEY = "Replaced_35cd1d4d"
MAILGUN_KEY = "Replaced_cd28cfc1"
AWS_ACCESS_KEY = "Replaced_496ac118"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# OAuth Configuration
OAUTH_CONFIG = {
    'client_id': '3MVG9IHF93JSQI2Zv012345678',
    'client_secret': 'Replaced_28a1fa24',
    'redirect_uri': 'http://localhost:5000/callback'
}

# Database connection (with credentials)
DATABASE_URL = "postgresql://admin:secretpass123@localhost:5432/testdb"

@app.route('/')
def home():
    return render_template('index.html', api_key=STRIPE_KEY)

@app.route('/api/users')
def get_users():
    # Basic auth header (hardcoded)
    auth_header = "Basic dXNlcm5hbWU6cGFzc3dvcmQ="
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/api/payment', methods=['POST'])
def process_payment():
    # Initialize Stripe with API key
    stripe.api_key = "Replaced_23ca1664"
    return jsonify({'status': 'success'})

@app.route('/api/auth')
def generate_token():
    # JWT secret key (hardcoded)
    SECRET_KEY = "Replaced_263b7867"
    token = jwt.encode(
        {'user_id': 123, 'exp': datetime.utcnow() + timedelta(hours=24)},
        SECRET_KEY,
        algorithm='HS256'
    )
    return jsonify({'token': token})

@app.route('/api/config')
def get_config():
    config = {
        'aws': {
            'access_key': AWS_ACCESS_KEY,
            'secret_key': AWS_SECRET_KEY,
            's3_bucket': 'my-test-bucket'
        },
        'sendgrid': {
            'api_key': 'Replaced_8eed46dc'
        },
        'github': {
            'token': 'Replaced_4a5d4157'
        }
    }
    return jsonify(config)

if __name__ == '__main__':
    cert_path = "server.crt"
    key_path = "Replaced_96b239ea"
    app.run(ssl_context=(cert_path, key_path), debug=True)
