from flask import Flask
from flask_restx import Api
from app.config import Config
from app.setup_db import db
from app.views.users import user_ns
from app.views.auth import auth_ns
from app.views.movies import movies_ns
from app.views.directors import directors_ns
from app.views.genres import genres_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def register_extensions(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    register_extensions(app)
    app.run(host='127.0.0.1', port=5000)
