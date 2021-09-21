from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config_options

db = SQLAlchemy()

def create_app(config_name):
    """This is the app factory
    """
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    db.init_app(app)

    from app.auth.v1 import auth
    app.register_blueprint(auth)

    return app