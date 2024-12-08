# config.py
class Config:
    SECRET_KEY = 'Replaced_d09d4dd9'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password123@localhost/testdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API Keys
    STRIPE_PUBLIC_KEY = 'Replaced_8bc7d59f'
    STRIPE_SECRET_KEY = 'Replaced_2fd25ed4'

    # OAuth credentials
    GOOGLE_CLIENT_ID = '740283726281-jc4hp6hd23f.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = 'Replaced_8b5822f0'
