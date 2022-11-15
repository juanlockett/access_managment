from flask_restful import Api, Resource
from flask import Blueprint

from app.common.error_handling import ObjectNotFound

from .schemas import AutorizationSchema
from ..models import Autorization

autorization_v1_0_bp = Blueprint('autorization_v1_0_bp', __name__)

autorization_schema = AutorizationSchema()

api = Api(autorization_v1_0_bp)



class AutorizationResource(Resource):

    def get(self, iduser):
        autorization = Autorization.get_by_id_user(iduser)
        if autorization is None:
            raise ObjectNotFound('El usuario{iduse} no existe')
        """
        for app in autorization.app:
            for sections in app.section:
                print(f'las secciones son:{sec}')
        """
        resp = autorization_schema.dump(autorization)

        return resp


api.add_resource(AutorizationResource, '/api/v1.0/autorizations/<int:iduser>', endpoint='autorizations_resource')
