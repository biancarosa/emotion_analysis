"""Deals with HealthCheck route."""
import os
import logging
import base64

import requests
from flask import jsonify

logging.basicConfig(level=logging.DEBUG)

def get_user_tweets():
    """Returns last 1000 user tweets"""
    screen_name = '__biancarosa'
    consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
    consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
    logging.debug(consumer_key)
    logging.debug(consumer_secret)
    r = requests.post(url='https://api.twitter.com/oauth2/token',
                          data={'grant_type': 'client_credentials'},
                          auth=(consumer_key, consumer_secret))
    auth_data = r.json()
    logging.debug(auth_data)
    token = auth_data["access_token"]
    logging.debug(token)
    r = requests.get(url=f'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={screen_name}&count=100',
                     headers={'Authorization': f'Bearer {token}'})
    return jsonify(r.json())
    