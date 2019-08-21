from flask import Blueprint
from flask_restful import Api

from .resources import RegisterUser

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)

api.add_resource(RegisterUser, '/users')
