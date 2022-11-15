from marshmallow import fields

from app.users.api_v1_0.schemas import UserSchema
from app.applications.api_v1_0.schemas import AppSectionSchema

from app.ext import ma

class AccessSchema(ma.Schema):

    idlevel = fields.Integer(dump_only=True)
    user = fields.Nested(UserSchema)
    app_section = fields.Nested(AppSectionSchema)
    