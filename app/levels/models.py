# coding: utf-8
from app.db import db, BaseModelMixin

class App(db.Model, BaseModelMixin):
    __tablename__ = 'app'

    idapp = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    apikey = db.Column(db.String(45))


class Level(db.Model, BaseModelMixin):
    __tablename__ = 'level'

    idlevel = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(45), nullable=False)
    name = db.Column(db.String(45))
    data = db.Column(db.String(45))
    label = db.Column(db.String(45))


    def __init__(self, type, name, data, label):
        self.type = type
        self.name = name
        self.data = data
        self.label = label


    def __repr__(self):
        return f'<Level(name={self.name})>'

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def get_all():
        return Level.query.all()


class System(db.Model, BaseModelMixin):
    __tablename__ = 'system'

    idsystem = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))


class User(db.Model, BaseModelMixin):
    __tablename__ = 'user'

    iduser = db.Column(db.Integer, primary_key=True)


class AppSection(db.Model, BaseModelMixin):
    __tablename__ = 'app_section'

    idapp_section = db.Column(db.Integer, primary_key=True)
    app_idapp = db.Column(db.ForeignKey('app.idapp'), nullable=False, index=True)
    name = db.Column(db.String(45))
    data = db.Column(db.String(45))

    app = db.relationship('App')


class Group(db.Model, BaseModelMixin):
    __tablename__ = 'group'

    idgroup = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    user_iduser = db.Column(db.ForeignKey('user.iduser'), nullable=False, index=True)

    user = db.relationship('User')


t_user__system = db.Table(
    'user__system', db.metadata,
    db.Column('user_iduser', db.ForeignKey('user.iduser'), nullable=False, index=True),
    db.Column('system_idsystem', db.ForeignKey('system.idsystem'), nullable=False, index=True),
    db.Column('user', db.String(45))
)


class Acces(db.Model, BaseModelMixin):
    __tablename__ = 'access'

    idaccess = db.Column(db.Integer, primary_key=True)
    group_idgroup = db.Column(db.ForeignKey('group.idgroup'), nullable=False, index=True)
    app_idapp = db.Column(db.ForeignKey('app.idapp'), nullable=False, index=True)

    app = db.relationship('App')
    group = db.relationship('Group')
    level = db.relationship('Level', secondary='level_access')


t_level_access = db.Table(
    'level_access', db.metadata,
    db.Column('access_idaccess', db.ForeignKey('access.idaccess'), primary_key=True, nullable=False, index=True),
    db.Column('level_idlevel', db.ForeignKey('level.idlevel'), primary_key=True, nullable=False, index=True)
)
