"""Default configuration

Use env var to override
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

ENV = os.getenv("FLASK_ENV")
DEBUG = ENV == "development"
SECRET_KEY = os.getenv("SECRET_KEY")
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_URL = os.getenv('POSTGRES_URL')
POSTGRES_DB = os.getenv('POSTGRES_DB')
SQLALCHEMY_DATABASE_URI = f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_URL}/{POSTGRES_DB}"

SQLALCHEMY_TRACK_MODIFICATIONS = False
