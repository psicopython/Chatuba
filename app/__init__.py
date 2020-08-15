from flask import Flask
from app.config import config

def create():
    app = Flask(__name__.split()[0])
    config(app)
    return app
