import os

from flask import Flask

from hometap_interview import exceptions
from hometap_interview.config import DevConfig


def create_app(config=None):
    # By default, if no config is provided use the DevConfig
    if not config:
        config = DevConfig

    app = Flask(__name__)
    app.config.from_object(config)
    app.logger.info(f"Created Flask app with {config} configuration")
    app.url_map.strict_slashes = False

    register_blueprints(app)

    @app.errorhandler(exceptions.NotFoundException)
    def handle_404(e):
        return {
            'message': str(e)
        }, 404

    @app.errorhandler(exceptions.RequiredParametersMissing)
    def handle_required_params_missing(e):
        return {
            'message': str(e)
        }, 400

    return app

def register_blueprints(app):
    """
    Register the views as flask blueprints
    """
    from hometap_interview.views import health, property_details
    app.register_blueprint(health.health_bp)
    app.register_blueprint(property_details.property_details_bp)