from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flaskr.app import app

db = SQLAlchemy(app)


class