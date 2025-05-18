import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    DEBUG=False
    TESTING=False

class DevConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.getenv('PROD_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI=os.getenv('DEV_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False