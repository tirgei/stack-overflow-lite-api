import os
from flask import Flask
from instance.config import app_config
from app.api.v1.views.user_views import auth, users

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    app.register_blueprint(auth)
    app.register_blueprint(users)

    return app