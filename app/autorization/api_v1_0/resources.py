from flask_restful import Api, Resource
from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.common.error_handling import ObjectNotFound

from .schemas import AutorizationSchema
from ..models import Autorization
from app.levels.api_v1_0.schemas import LevelSchema

autorization_v1_0_bp = Blueprint('autorization_v1_0_bp', __name__)

autorization_schema = AutorizationSchema()
level_schema = LevelSchema()

api = Api(autorization_v1_0_bp)


class AutorizationResource(Resource):

    @jwt_required()
    def get(self, iduser):
        autorization = Autorization.get_by_id_user(iduser)
        if autorization is None:
            raise ObjectNotFound('El usuario{iduse} no existe')

        resp = autorization_schema.dump(autorization)

        return resp







api.add_resource(AutorizationResource, '/api/v1.0/autorizations/<int:iduser>', endpoint='autorizations_resource')
