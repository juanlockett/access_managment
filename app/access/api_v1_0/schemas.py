from marshmallow import fields

from app.ext import ma

class AccessSchema(ma.Schema):

    idlevel = fields.Integer(dump_only=True)
    user_iduser = fields.Integer(dum_only=True)
    app_section_idapp_section = fields.Integer(dump_only=True)
    