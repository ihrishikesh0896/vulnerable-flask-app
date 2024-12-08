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
STRIPE_KEY = "Replaced_10fd82f7"
MAILGUN_KEY = "Replaced_531d31c7"
AWS_ACCESS_KEY = "Replaced_f1c5f4d1"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# OAuth Configuration
OAUTH_CONFIG = {
    'client_id': '3MVG9IHF93JSQI2Zv012345678',
    'client_secret': 'Replaced_29dfedf4',
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
    stripe.api_key = "Replaced_4fd4653f"
    return jsonify({'status': 'success'})

@app.route('/api/auth')
def generate_token():
    # JWT secret key (hardcoded)
    SECRET_KEY = "Replaced_69c54cdc"
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
            'api_key': 'Replaced_1e1e6c74'
        },
        'github': {
            'token': 'Replaced_d0b710da'
        }
    }
    return jsonify(config)

if __name__ == '__main__':
    cert_path = "server.crt"
    key_path = "Replaced_85361fd0"
    app.run(ssl_context=(cert_path, key_path), debug=True)
