from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from flask_cors import CORS

from app.common.error_handling import ObjectNotFound, AppErrorBaseClass
from app.db import db

from app.levels.api_v1_0.resources import levels_v1_0_bp
from app.applications.api_v1_0.resources import app_v1_0_bp
from app.access.api_v1_0.resources import access_v1_0_bp
from app.autorization.api_v1_0.resources import autorization_v1_0_bp
from app.autentication.api_v1_0.resources import autentication_v1_0_bp

from .ext import ma, migrate



def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)

    CORS(app, resources={ r'/*': { 'origins': '*', 'methods': ['POST', 'GET', 'PUT', 'DELETE', ]}})

    # Config JWT
    #app.config["JWT_SECRET_KEY"]
    jwt = JWTManager(app)

    #Inicializa las extenciones
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    #capturar errores
    Api(app, catch_all_404s=True)

    #Desabilitar el modo estricto de acabado de una URL con /
    app.url_map.strict_slashes = False

    #Registrar los blueprints
    app.register_blueprint(levels_v1_0_bp)
    app.register_blueprint(app_v1_0_bp)
    app.register_blueprint(access_v1_0_bp)
    app.register_blueprint(autorization_v1_0_bp)
    app.register_blueprint(autentication_v1_0_bp)

    #Registrar manejadores de error
    register_error_handlers(app)

    
    return app


def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        return jsonify({'msg': 'Internal server error'}), 500

    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({'msg': 'Method not allow'}), 405

    @app.errorhandler(403)
    def handler_403_error(e):
        return jsonify({'msg': 'Forbidden error'}), 403

    @app.errorhandler(404)
    def handler_404_error(e):
        return jsonify({'msg': 'Not Found error'}), 404

    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(e):
        return jsonify({'msg': str(e)}), 500

    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        return jsonify({'msg': str(e)}), 404
