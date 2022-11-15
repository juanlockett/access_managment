from app.db import db, BaseModelMixin
from app.applications.models import App, AppSection
from app.users.models import User
from app.access.models import Access, t_level_access




class AbstractApp():

    section = []

    def __init__(self, id, name, newSection=None):
        self.id = id
        self.name = name
        self.section = []
        if newSection:
            self.section = self.section.append(newSection)


    def add_section(self, section):
        self.section.append(section)


    def __repr__(self) -> str:
        return f'<App(id={self.id}, name={self.name})>'


    def __str__(self) -> str:
        return f'<App(id={self.id}, name={self.name})>'


class AbstractAppSection():

    def __init__(self, id, name, data):
        self.id = id
        self.name = name
        self.data = data

    
    def __repr__(self) -> str:
        return f'<AppSection(id={self.id}, name={self.name}, data={self.data})>'


    def __str__(self) -> str:
        return f'<AppSection(id={self.id}, name={self.name}, data={self.data})>'


class AbstractUser():

    def __init__(self, id, app, name=None):
        self.id = id,
        self.name = name
        self.app = app

    def add_app(self, app):
        for sapp in self.app:
            if sapp.id == app.id:
                pass
        pass

    def get_app(self):
        return self.app


class Autorization():

    app = []

    def __init__(self, iduser, apps=None):

        self.iduser = iduser
        if apps:
            self.app = self.app.append(apps)
        else:
            self.app = []


    def __str__(self) -> str:
        return f'<Autorization(iduser={self.iduser}, app={self.app})>'

    
    def add_app(self, app):
        self.app.append(app)


    def update_app(self, abstapp):
        
        for app in self.app:
            if abstapp.id == app.id:
                print(f'###>>>new sections is: {abstapp.section}')
                app.add_section(abstapp.section)

                return

        self.app.append(abstapp)

        return
    


    @staticmethod
    def get_by_id_user(iduser):

        obj_autorization = Autorization(iduser)
        ls_obj_access = Access.simple_filter(user_iduser=iduser)

        for obj_access in ls_obj_access:

            obj_app_section = AppSection.get_by_id(obj_access.app_section_idapp_section)
            print(f'###appSection>>>{obj_app_section}')
            obj_abstr_app_section = AbstractAppSection(obj_app_section.idapp_section, obj_app_section.name, obj_app_section.data)
            print(f'###>>> abstract section: {obj_abstr_app_section}')
            obj_app = App.get_by_id(obj_app_section.app_idapp)
            obj_abstr_app = AbstractApp(obj_app.idapp, obj_app.name, obj_abstr_app_section)
            print(f'the app is: {obj_abstr_app}')
            obj_autorization.update_app(obj_abstr_app)

        return obj_autorization


    