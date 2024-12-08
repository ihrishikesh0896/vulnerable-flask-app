# config.py
class Config:
    SECRET_KEY = 'Replaced_73b4f897'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password123@localhost/testdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API Keys
    STRIPE_PUBLIC_KEY = 'Replaced_c00120dc'
    STRIPE_SECRET_KEY = 'Replaced_3c136ddd'

    # OAuth credentials
    GOOGLE_CLIENT_ID = '740283726281-jc4hp6hd23f.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = 'Replaced_2f48df56'
