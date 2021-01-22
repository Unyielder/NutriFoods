import os
from flask import Flask
from flaskr.controllers import auth
from flaskr.controllers import home

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)


# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from . import db
db.init_app(app)

# Registering blueprints
app.register_blueprint(auth.bp)
app.register_blueprint(home.bp)

