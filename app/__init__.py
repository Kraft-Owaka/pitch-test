from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    #....
    #Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)


bootstrap = Bootstrap()

def create_app(config_name):
    # Initializing application
    app = Flask(__name__,instance_relative_config = True)


    # Setting up configuration
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    # Initializing Flask Extensions
    bootstrap.init_app(app)
    
    # Registering the blueprint
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app