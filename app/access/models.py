from app.db import db, BaseModelMixin
from app.applications.models import App, AppSection
#from app.users.models import User <-- debe estar construído el modelo de usuario


class Access(db.Model, BaseModelMixin):
    __tablename__ = 'access'

    idaccess = db.Column(db.Integer, primary_key=True)
    user_iduser = db.Column(db.ForeignKey('user.iduser'), nullable=False, index=True)
    app_section_idapp_section = db.Column(db.ForeignKey('app_section.idapp_section'), nullable=False, index=True)

    app_section = db.relationship('AppSection')
    user = db.relationship('User')
    level = db.relationship('Level', secondary='level_access')

    @staticmethod
    def get_by_user(self, user_id):
        #Access.self.query.filter_by_user(Access.query.user(user_id).join)
        pass

t_level_access = db.Table(
    'level_access', db.metadata,
    db.Column('access_idaccess', db.ForeignKey('access.idaccess'), primary_key=True, nullable=False, index=True),
    db.Column('level_idlevel', db.ForeignKey('level.idlevel'), primary_key=True, nullable=False, index=True)
)
