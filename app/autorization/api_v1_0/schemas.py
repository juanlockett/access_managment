from marshmallow import fields

from app.levels.api_v1_0.schemas import LevelSchema
from app.ext import ma



class AbstractAppSectionSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()
    data = fields.String()
    levels = fields.Nested(LevelSchema, many=True)



class AbstractAppSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()
    section = fields.Nested(AbstractAppSectionSchema, many=True)



class AutorizationSchema(ma.Schema):
    iduser = fields.Integer()
    app = fields.Nested(AbstractAppSchema, many=True)