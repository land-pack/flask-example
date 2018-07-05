from flask import Flask
from config import config


def create_app(config_name='base'):
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_object(config[config_name])
    app.config.from_pyfile('/home/frank/PycharmProjects/SeeleCMS/project/flask.cfg')

    # import Blueprins
    from project.article.views import article_blueprint
    from project.users.views import users_blueprint

    # register the blueprints
    app.register_blueprint(users_blueprint)
    app.register_blueprint(article_blueprint)
    print('register blue print successful')
    return app
