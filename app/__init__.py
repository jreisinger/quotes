from flask import Flask
from config import config
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    """
    The application factory - allows for:

        * dynamic configuration
        * multiple app instances

    It returns the created app instance.
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)

    """
    A blueprint is similar to an application in that it can also define routes
    and error handlers. But they are dormant until the blueprint is registered
    with an application. Then they become part of the app.
    """

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
