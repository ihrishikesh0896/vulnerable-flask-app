# config.py
class Config:
    SECRET_KEY = 'Replaced_47a06a0a'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password123@localhost/testdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API Keys
    STRIPE_PUBLIC_KEY = 'Replaced_2646ab58'
    STRIPE_SECRET_KEY = 'Replaced_e06b9508'

    # OAuth credentials
    GOOGLE_CLIENT_ID = '740283726281-jc4hp6hd23f.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = 'Replaced_5a5aa70c'
