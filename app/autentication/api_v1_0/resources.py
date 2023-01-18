from flask import request, Blueprint
from app.common.error_handling import ObjectNotFound
from flask_restful import Api, Resource

from .schemas import CredentialsSchema, AccessTokenSchema
from ..models import Autentication, AccessToken

from flask_jwt_extended import create_access_token



autentication_v1_0_bp = Blueprint('autentication_v1_0_bp', __name__)

#autentication_schema = AutenticationSchema()
credentials_schema = CredentialsSchema()
accessTocken_schema = AccessTokenSchema()

api=Api(autentication_v1_0_bp)


class AutenticationResource(Resource):

    def get(self):
        return 405

    def post(self):
        data = request.get_json()
        credentials_dict = credentials_schema.load(data)

        autentication = Autentication.get_by_credentials(username=credentials_dict['user'], password=credentials_dict['password'])

        if not autentication:
            raise ObjectNotFound('credenciales no encontradas')

        #print(autentication)
        access_token = AccessToken(create_access_token(identity=autentication.user_iduser))
        #print(f'Tipe object {type(access_token)} con valor {access_token}')
        resp = accessTocken_schema.dump(access_token)
        #print(f'dump del token {resp}')
        return resp

api.add_resource(AutenticationResource, '/api/v1.0/autentication/', endpoint='autentication_resource', methods=['GET', 'POST',])

        

