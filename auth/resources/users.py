from flask import request
from flask_restful import Resource
from ..models import User
from extentions import db, ma


class UserSchema(ma.ModelSchema):
    password = ma.String(load_only=True, required=True)

    class Meta:
        model = User


class RegisterUser(Resource):
    """Single object resource
    """
    schema = UserSchema()

    def post(self):
        user_data = request.get_json()
        username = user_data['user']["username"]
        password = user_data['user']["password"]
        email = user_data['user']["email"]
        schema = self.schema
        user = User(
            username=username,
            password=password,
            email=email,
        )
        user, errors = schema.load(request.json.get('user'), instance=user)
        if errors:
            return errors, 422
        db.session.add(user)
        db.session.commit()
        return_data = User.query.filter_by(email=email).first()

        return {"user": schema.dump(return_data).data}

    def get(self):
        schema = self.schema
        users = User.query.all()
        return {"user": schema.dump(users, many=True).data}
