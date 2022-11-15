from flask import request, Blueprint
from app.common.error_handling import ObjectNotFound
from flask_restful import Api, Resource

from .schemas import AccessSchema
from ..models import Access

access_v1_0_bp = Blueprint('access_v1_0_bp', __name__)

access_schema = AccessSchema()

api = Api(access_v1_0_bp)

class AccessListResource(Resource):
    
    def get(self):
        access = Access.get_all()
        result = access_schema.dump(access, many=True)

        return result

    def post(self):
        data = request.get_json()
        access_dict = access_schema.load(data)
        access = Access()

        access.save()
        resp = access_schema.dump(access)

        return resp, 201

class AutorizationAccessList(Resource):

    def get(self):
        autorization = Access.getAutorizationAccess_byUserId(1)
        print(autorization)
        result = access_schema.dump(autorization, many=True)

        return result

class AccessResource(Resource):
    def get(self, access_id):
        access = Access.get_by_id(access_id)
        if access is None:
            raise ObjectNotFound(f'Access id{access_id} not found')

        resp = access_schema.dump(access)

        return resp


class AccessUserResource(Resource):
    def get(self, user_id):
        access = Access.simple_filter(user_id)
        pass




api.add_resource(AccessListResource, '/api/v1.0/access/', endpoint='access_list_resource')
api.add_resource(AccessResource, '/api/v1.0/access/<int:access_id>', endpoint='access_resource')
api.add_resource(AccessUserResource, '/api/v1.0/access/levelAccessApp/<int:user_id>', endpoint='level_access_app')
api.add_resource(AutorizationAccessList, '/api/v1.0/access/autorizationAccess/', endpoint='autorization_access')