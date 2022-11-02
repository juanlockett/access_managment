from urllib import response
from flask import request, Blueprint
from app.common.error_handling import ObjectNotFound
from flask_restful import Api, Resource

from .schemas import AppSchema, AppSectionSchema
from ..models import App, AppSection

app_v1_0_bp = Blueprint('app_v1_0_bp', __name__)

app_schema = AppSchema()
appSection_schema = AppSectionSchema()

api = Api(app_v1_0_bp)


class AppListResource(Resource):

    def get(self):
        apps = App.get_all()
        result = app_schema.dump(apps, many=True)

        return result

    def post(self):
        data = request.get_json()
        app_dict = app_schema.load(data)
        app = App(
                name=app_dict['name'],
                description=app_dict['description']
        )
        for appSection in app_dict['sections']: #check name in te object
            app.section.append(AppSection(appSection['name'], appSection['data']))

        app.save()
        resp = app_schema.dump(app)

        return resp, 201


class AppResource(Resource):
    
    def get(self, app_id):
        app = App.get_by_id(app_id)
        if app is None:
            raise ObjectNotFound('El nivel no existe')
            
        resp = app_schema.dump(app)

        return resp



class AppSectionListResource(Resource):
    pass



class AppSectionResource(Resource):
    
    def get(self):
        appsSections = AppSection.get_all()
        result = appSection_schema.dump(appsSections, many=True)

        return result


    def post(self):
        data = request.get_json()
        appSection_dict = appSection_schema.load(data)
        appSection = AppSection(
            name = appSection_dict['name'],
            data = appSection_dict['data']
        )

        appSection.save()
        resp = appSection_schema.dump(appSection)

        return resp, 201



api.add_resource(AppListResource, '/api/v1.0/apps/', endpoint='app_list_resource')
api.add_resource(AppResource, '/api/v1.0/apps/<int:app_id>', endpoint='app_resource')