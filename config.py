# config.py
class Config:
    SECRET_KEY = 'Replaced_42fff172'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password123@localhost/testdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API Keys
    STRIPE_PUBLIC_KEY = 'Replaced_90f800f6'
    STRIPE_SECRET_KEY = 'Replaced_d34f2fa1'

    # OAuth credentials
    GOOGLE_CLIENT_ID = '740283726281-jc4hp6hd23f.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = 'Replaced_d2c27828'
