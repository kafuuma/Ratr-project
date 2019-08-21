import click
from flask.cli import FlaskGroup
from src import create_app
from os import getenv


def create_ratr_app(info=None):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_ratr_app)
def cli():
    """Main entry point"""
    pass


@cli.command()
def init():
    """Init application, create database tables
    and create a new user named admin with password admin
    """
    from src.extensions import db
    from src.api.models import User
    from sqlalchemy_utils import database_exists, create_database

    DB_URL = f"postgres://{getenv('POSTGRES_USER')}:{getenv('POSTGRES_PASSWORD')}@{getenv('POSTGRES_URL')}/{getenv('POSTGRES_DB')}" # noqa
    if not database_exists(DB_URL):
        click.echo("create database")
        create_database(DB_URL)

    db.create_all()
    click.echo("done")

    click.echo("create user")
    user = User(username='admin1',
                email='admin2@mail.com',
                password='admin2',
                active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


if __name__ == "__main__":
    cli()
