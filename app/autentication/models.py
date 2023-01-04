from app.db import db, BaseModelMixin

from app.users.models import User

class Autentication(db.Model, BaseModelMixin):
    __tablename__ = 'password'

    idpassword = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(255))
    user_iduser = db.Column(db.ForeignKey('user.iduser'), nullable=False, index=True)

    user = db.relationship('User', foreign_keys='Autentication.user_iduser')
    
    def __repr__(self):
        return f'<Autentication(id={self.idpassword}, user={self.user}, user_iduser={self.user_iduser})>'


    def __str__(self):
        return f'<Autentication(id={self.idpassword}, user={self.user}, user_iduser={self.user_iduser})>'

    @staticmethod
    def get_by_credentials(username, password):
        return Autentication().query.filter_by(username=username, password=password).first()


class AccessToken():

    access_token = ''

    def __init__(self, access_token):
        self.access_token = access_token

    def __repr__(self):
        return f'<AccessToken(access_token={self.access_token})>'

    def __str__(self):
        return f'<AccessToken(access_token={self.access_token})>'