from marshmallow import fields

from app.ext import ma

class AppSchema(ma.Schema):

    idapp = fields.Integer(dump_only=True)
    name = fields.String()
    description = fields.String()


class AppSectionSchema(ma.Schema):

    idapp_section = fields.Integer(dump_only=True)
    app_idapp = fields.Nested(AppSchema, many=True)
    name = fields.String()
    data = fields.String()