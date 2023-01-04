from marshmallow import fields

from app.ext import ma

class CredentialsSchema(ma.Schema):

    user = fields.String()
    password = fields.String()


class AccessTokenSchema(ma.Schema):
    access_token = fields.Str()