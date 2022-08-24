from marshmallow import fields

from app.ext import ma

class LevelSchema(ma.Schema):

    idlevel = fields.Integer(dump_only=True)
    type = fields.String()
    name = fields.String()
    data = fields.String()
    label = fields.String()

