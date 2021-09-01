import traceback
from os import path

from flask import Flask
from flask_login import LoginManager
from py_profiler.profiler_controller import profiler_blueprint

from .auth import auth
from .models import User
from .models import db, DB_NAME
from .views import views


def handle_exceptions(error):
    print('xxxxxxxxxxxxxxx')
    if error.__cause__ is not None:
        print("".join(traceback.TracebackException.from_exception(error.__cause__).format()))
    else:
        print(error)


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.register_error_handler(Exception, handle_exceptions)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    # Add blueprint to view profiler page
    app.register_blueprint(profiler_blueprint)

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    print(app.url_map)

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
