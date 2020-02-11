from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    # Initializing application
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    # Initializing Flask Extensions
    bootstrap.init_app(app)
    
    # Registering the blueprint
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return 