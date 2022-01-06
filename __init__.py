import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='DEV'
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )