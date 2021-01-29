from flask import Flask
from flaskr.model import User
from flaskr.db import db_session
from flask_login import LoginManager

app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = r"sqlite:///C:\Users\Mohamed\PycharmProjects\Meal " \
                                        r"Prep\instance\Canadian_Foods.db "
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Registering blueprints
from flaskr.controllers import auth
from flaskr.controllers import home

app.register_blueprint(auth.bp)
app.register_blueprint(home.bp)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
