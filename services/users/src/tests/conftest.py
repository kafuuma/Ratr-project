import os
import tempfile

import pytest
import json

from src import create_app
from ..extensions import db as _db
from ..api.models import User

from sqlalchemy_utils import create_database, drop_database


@pytest.fixture
def client():
    app = create_app(testing=True)
    DATABASE_URI = 'sqlite:///Ratr.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    with app.test_client() as client:
        with app.app_context():
            create_database(DATABASE_URI)
            _db.create_all()
        yield client

        with app.app_context():
            _db.session.close()
            _db.drop_all()
            drop_database(DATABASE_URI)
