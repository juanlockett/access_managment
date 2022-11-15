from app.db import db, BaseModelMixin
from app.applications.models import App


class User(db.Model, BaseModelMixin):
    __tablename__ = 'user'

    iduser = db.Column(db.Integer, primary_key=True)


class Credentials(db.Model, BaseModelMixin):
    __tablename__ = 'credentials'

    idcredentials = db.Column(db.Integer, primary_key=True)
    apikey = db.Column(db.String())

    user_iduser = db.Column(db.ForeignKey('user.iduser'), nullable=False, index=True)
    app_idapp = db.Column(db.ForeignKey('app.idapp'), nullable=False, index=True)

    user = db.relationship('User')
    app = db.relationship('App')