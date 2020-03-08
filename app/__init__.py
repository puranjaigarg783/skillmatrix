import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'authn.log_in'
bcrypt = Bcrypt()


def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)


    from app.plogin import pdash
    app.register_blueprint(pdash)

    from app.auth import authn
    app.register_blueprint(authn)

    from app.filter import filtr
    app.register_blueprint(filtr)

    from app.edit import edit
    app.register_blueprint(edit)

    return app
