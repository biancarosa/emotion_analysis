"""Deals with Blueprint-related stuff."""
from flask import Blueprint
from app.data import tweets

def create_blueprint():
    """Creates a Blueprint"""
    blueprint = Blueprint('Data Blueprint', __name__)
    blueprint.route('/user/tweets')(tweets.get_user_tweets)
    return blueprint
