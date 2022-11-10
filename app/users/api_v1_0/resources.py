from urllib import response
from flask import request, Blueprint
from app.common.error_handling import ObjectNotFound
from flask_restful import Api, Resource

from .schemas import UserSchema
from ..models import User

users_v1_0_bp = Blueprint('users_v1_0_bp', __name__)

user_schema = UserSchema()

api = Api(users_v1_0_bp)


class UserResource(Resource):

    def get(self, user_id):
        user = User.get_by_id(user_id)
        if user is None:
            raise ObjectNotFound(f'User id{user_id} not found')

        resp = user_schema.dump(user)

        return resp, 201



api.add_resource(UserResource, '/api/v1.0/user/<int:user_id>', endpoint='user_resource')