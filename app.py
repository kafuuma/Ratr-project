from flask import Flask
from extentions import db, migrate, ma
from auth import views


def create_app(testing=False, cli=False):
    """Application factory used to ceate app"""
    app = Flask(__name__)
    app.config.from_object('config')
    if testing:
        app.config['TESTING'] = True
    configure_extensions(app, cli)
    register_blueprints(app)

    return app


def configure_extensions(app, cli):
    """Configure flask extentions"""
    db.init_app(app)
    ma.init_app(app)
    if cli:
        migrate.init_app(app, db)


def register_blueprints(app):
    """Register blue prints for application"""
    app.register_blueprint(views.blueprint)
