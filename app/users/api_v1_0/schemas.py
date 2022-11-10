from marshmallow import fields

from app.ext import ma

class UserSchema(ma.Schema):

    iduser = fields.Integer(dump_only=True)
