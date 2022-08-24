# coding: utf-8
from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class App(Base):
    __tablename__ = 'app'

    idapp = Column(INTEGER(11), primary_key=True)
    name = Column(String(45))
    apikey = Column(String(45))


class Level(Base):
    __tablename__ = 'level'

    idlevel = Column(INTEGER(11), primary_key=True)
    type = Column(String(45), nullable=False)
    name = Column(String(45))
    data = Column(String(45))
    label = Column(String(45))


class System(Base):
    __tablename__ = 'system'

    idsystem = Column(INTEGER(11), primary_key=True)
    name = Column(String(45))


class User(Base):
    __tablename__ = 'user'

    iduser = Column(INTEGER(11), primary_key=True)


class AppSection(Base):
    __tablename__ = 'app_section'

    idapp_section = Column(INTEGER(11), primary_key=True)
    app_idapp = Column(ForeignKey('app.idapp'), nullable=False, index=True)
    name = Column(String(45))
    data = Column(String(45))

    app = relationship('App')


class Group(Base):
    __tablename__ = 'group'

    idgroup = Column(INTEGER(11), primary_key=True)
    name = Column(String(45))
    user_iduser = Column(ForeignKey('user.iduser'), nullable=False, index=True)

    user = relationship('User')


t_user__system = Table(
    'user__system', metadata,
    Column('user_iduser', ForeignKey('user.iduser'), nullable=False, index=True),
    Column('system_idsystem', ForeignKey('system.idsystem'), nullable=False, index=True),
    Column('user', String(45))
)


class Acces(Base):
    __tablename__ = 'access'

    idaccess = Column(INTEGER(11), primary_key=True)
    group_idgroup = Column(ForeignKey('group.idgroup'), nullable=False, index=True)
    app_idapp = Column(ForeignKey('app.idapp'), nullable=False, index=True)

    app = relationship('App')
    group = relationship('Group')
    level = relationship('Level', secondary='level_access')


t_level_access = Table(
    'level_access', metadata,
    Column('access_idaccess', ForeignKey('access.idaccess'), primary_key=True, nullable=False, index=True),
    Column('level_idlevel', ForeignKey('level.idlevel'), primary_key=True, nullable=False, index=True)
)
