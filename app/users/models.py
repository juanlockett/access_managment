from app.db import db, BaseModelMixin


class User(db.Model, BaseModelMixin):
    __tablename__ = 'user'

    iduser = db.Column(db.Integer, primary_key=True)


class Credentials(db.Model, BaseModelMixin):
    apikey = db.Column(db.String())
    user_iduser = db.Column(db.ForeingKey('user.iduser'), nullable=False, index=True)
    app_idapp = db.Column(db.ForeingKey('app.idapp'), nullable=False, index=True)

    user = db.relationship('User')
    app = db.relationship('App')