import os
class Config:
    pjdir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(pjdir, 'main/static/db/data2.sqlite')
    SECRET_KEY = 'wahahaha'
    SESSION_PROTECTION = 'strong'