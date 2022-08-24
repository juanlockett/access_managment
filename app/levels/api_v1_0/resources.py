from urllib import response
from flask import request, Blueprint
from app.common.error_handling import ObjectNotFound
from flask_restful import Api, Resource

from .schemas import LevelSchema
from ..models import Level

levels_v1_0_bp = Blueprint('levels_v1_0_bp', __name__)

level_schema = LevelSchema()

api = Api(levels_v1_0_bp)


class LevelListResource(Resource):

    def get(self):
        levels = Level.get_all()
            
        result = level_schema.dump(levels, many=True)

        return result

    def post(self):
        data = request.get_json()
        level_dict = level_schema.load(data)
        level = Level(type=level_dict['type'],
                      name=level_dict['name'],
                      data=level_dict['data'],
                      label=level_dict['label']
        )

        level.save()
        resp = level_schema.dump(level)

        return resp, 201


class LevelResource(Resource):
    
    def get(self, level_id):
        level = Level.get_by_id(level_id)
        if level is None:
            raise ObjectNotFound('El nivel no existe')
            
        resp = level_schema.dump(level)

        return resp



api.add_resource(LevelListResource, '/api/v1.0/levels/', endpoint='level_list_resource')
api.add_resource(LevelResource, '/api/v1.0/levels/<int:level_id>', endpoint='level_resource')