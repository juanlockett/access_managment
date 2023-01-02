from urllib import response
from flask import request, Blueprint
from app.common.error_handling import ObjectNotFound
from flask_restful import Api, Resource

from .schemas import AutenticationSchema
from ..models import Autentication

app_v1_0_bp = Blueprint('app_v1_0_bp', __name__)

autentication_schema = AutenticationSchema()

api=Api(app_v1_0_bp)