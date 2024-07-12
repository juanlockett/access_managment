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


class AppResource(Resource):
    
    def get(self, app_id):
        app = App.get_by_id(app_id)
        if app is None:
            raise ObjectNotFound('El nivel no existe')
            
        resp = app_schema.dump(app)

        return resp
    
    def post(self):
        data = request.get_json()
        app_dict = app_schema.load(data)
        app = App(
            name=app_dict['name'],
        )

        app.save()
        resp = app_schema.dump(app)

        return resp, 201



class AppSectionListResource(Resource):
    def get(self):
        appSections = AppSection.get_all()
        result = appSection_schema(appSections, many=True)

        return result



class AppSectionResource(Resource):
    
    def get(self):
        appsSections = AppSection.get_all()
        result = appSection_schema.dump(appsSections, many=True)

        return result


    def post(self, app_id):
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
api.add_resource(AppResource, '/api/v1.0/app/<int:app_id>', '/api/v1.0/app/', endpoint='app_resource')
api.add_resource(AppSectionResource, '/api/v1.0/appsection/<int:app_id>', '/api/v1.0/appsection/', endpoint='app__section_resource')