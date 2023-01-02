from app.db import db, BaseModelMixin

class Autentication(db.Model, BaseModelMixin):
    __table__ = 'password'

    idpassword = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(64))
    password = db.Column(db.String(255))
    user_iduser = db.Column(db.ForeingKey('user.iduser'), nullable=False, index=True)

    user = db.relationship('User', foreing_key='user_iduser')

    def __repr__(self):
        return f'<Autentication(id={self.idpassword}, user={self.user}, user_iduser={self.user_iduser})>'


    def __str__(self):
        return f'<Autentication(id={self.idpassword}, user={self.user}, user_iduser={self.user_iduser})>'