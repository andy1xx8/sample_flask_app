from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import traceback

from . import db, DB_NAME

def handle_other_exceptions(error):
    print('xxxxxxxxxxxxxxx')
    print(error)

    if error.__cause__ is not None:
        print("".join(traceback.TracebackException.from_exception(error.__cause__).format()))
    else:
        print(error.message)

def create_app():
    app = Flask(__name__)
    app.debug = True
    app.register_error_handler(Exception, handle_other_exceptions)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    from .models import User, Note

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
