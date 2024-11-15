# config.py
class Config:
    SECRET_KEY = 'dev-secret-key-123'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password123@localhost/testdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API Keys
    STRIPE_PUBLIC_KEY = 'pk_test_51HB8x9CJJ2PtpSAZ'
    STRIPE_SECRET_KEY = 'sk_test_51HB8x9CJJ2PtpSAZ'

    # OAuth credentials
    GOOGLE_CLIENT_ID = '740283726281-jc4hp6hd23f.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = 'GOCSPX-2HE9_9zdB7mj3kN'
