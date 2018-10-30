# encoding: utf-8
"""Application.

Starts the Flask application
"""
from flask import Flask

from app.healthcheck import blueprint as health_check_blueprint
from app.data import blueprint as data_blueprint

# pylint: disable=C0103
app = Flask(__name__)
app.register_blueprint(health_check_blueprint.create_blueprint())
app.register_blueprint(data_blueprint.create_blueprint())
