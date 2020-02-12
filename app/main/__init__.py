from flask import Blueprint
main = Blueprint('main', __name__)
from . import views, error


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    db.init_app(app)

    return app