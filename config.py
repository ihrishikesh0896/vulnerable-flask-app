# config.py
class Config:
    SECRET_KEY = 'Replaced_d174bcc5'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password123@localhost/testdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API Keys
    STRIPE_PUBLIC_KEY = 'Replaced_f26fbdf3'
    STRIPE_SECRET_KEY = 'Replaced_ce6e44c2'

    # OAuth credentials
    GOOGLE_CLIENT_ID = '740283726281-jc4hp6hd23f.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = 'Replaced_e9007437'
