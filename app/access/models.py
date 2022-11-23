from app.db import db, BaseModelMixin
from app.applications.models import App, AppSection
from app.users.models import User
from app.levels.models import Level


t_level_access = db.Table(
    'level_access', db.metadata,
    db.Column('access_idaccess', db.ForeignKey('access.idaccess'), primary_key=True, nullable=False, index=True),
    db.Column('level_idlevel', db.ForeignKey('level.idlevel'), primary_key=True, nullable=False, index=True)
)



class Access(db.Model, BaseModelMixin):
    __tablename__ = 'access'

    idaccess = db.Column(db.Integer, primary_key=True)
    user_iduser = db.Column(db.ForeignKey('user.iduser'), nullable=False, index=True)
    app_section_idapp_section = db.Column(db.ForeignKey('app_section.idapp_section'), nullable=False, index=True)

    app_section = db.relationship("AppSection", foreign_keys="[Access.app_section_idapp_section]")
    user = db.relationship("User", foreign_keys="[Access.user_iduser]")
    level = db.relationship("Level", secondary=t_level_access, backref='access_idaccess')


    def __init__(self, user_iduser, app_sectio_idapp_section):
        self.app_sectio_idapp_section = app_sectio_idapp_section
        self.user_iduser = user_iduser


    def __repr__(self):
        return f'<Access(idaccess={self.idaccess}, app_section={self.app_section}, user={self.user})>'


    def __str__(self):
        return f'<Access(idaccess={self.idaccess}, app_section={self.app_section}, user={self.user})>'

    @staticmethod
    def get_autorization_access():
        
        return db.Query(Access).join(AppSection, Access.app_section_idapp_section==AppSection.idapp_section).all()


