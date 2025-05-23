from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os

load_dotenv()
migrate = Migrate()
db = SQLAlchemy()
jwt = JWTManager()

def create_app():

    app = Flask(__name__)

    env = os.getenv('FLASK_ENV')

    if env == 'production':
        from app.config import ProdConfig
        app.config.from_object(ProdConfig)
    elif env == 'testing':
        from app.config import TestConfig
        app.config.from_object(TestConfig)
    else:
        from app.config import DevConfig
        app.config.from_object(DevConfig)


    migrate.init_app(app=app, db=db)
    db.init_app(app=app)

    return app