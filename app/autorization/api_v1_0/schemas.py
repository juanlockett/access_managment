from marshmallow import fields

from app.ext import ma


class AbstractAppSectionSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()
    data = fields.String()



class AbstractAppSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()
    section = fields.Nested(AbstractAppSectionSchema, many=True)



class AutorizationSchema(ma.Schema):
    iduser = fields.Integer()
    app = fields.Nested(AbstractAppSchema, many=True)