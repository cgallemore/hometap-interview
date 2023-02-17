import os

from flask import Flask


def create_app():
    # create and configure the app
    app = Flask(__name__)

    from .views import health
    app.register_blueprint(health.health_bp)

    return app