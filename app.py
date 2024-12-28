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
STRIPE_KEY = "sk_live_51NBK2JGI8iCEF234fdsa789"
MAILGUN_KEY = "key-3ax6xnjp29jd6fds4gc373sgvjxteol0"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# OAuth Configuration
OAUTH_CONFIG = {
    'client_id': '3MVG9IHF93JSQI2Zv012345678',
    'client_secret': '9u8A7b6C5d4E3F2G1',
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
    stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"
    return jsonify({'status': 'success'})

@app.route('/api/auth')
def generate_token():
    # JWT secret key (hardcoded)
    SECRET_KEY = "your-256-bit-secret-key-here"
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
            'api_key': 'SG.pKwD24NsRqy6r8RH9bX0DA.8xDqI0JwDAS4cl8d6PrjeV'
        },
        'github': {
            'token': 'ghp_kd8392jf8sdf723hj2k3h42'
        }
    }
    return jsonify(config)

if __name__ == '__main__':
    # cert_path = "server.crt"
    # key_path = "server.key"
    app.run(ssl_context=(cert_path, key_path), debug=True)
