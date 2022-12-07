from app.db import db, BaseModelMixin
from app.applications.models import App, AppSection
from app.users.models import User
from app.access.models import Access, t_level_access
from app.levels.models import Level




class AbstractApp():

    section = []

    def __init__(self, id, name, newSection):
        self.id = id
        self.name = name
        self.section = []
        if newSection:
            self.section.append(newSection)


    def add_section(self, section):
        self.section.append(section)


    def __repr__(self) -> str:
        return f'<App(id={self.id}, name={self.name}, section={self.section})>'


    def __str__(self) -> str:
        return f'<App(id={self.id}, name={self.name}, section={self.section})>'


class AbstractAppSection():

    def __init__(self, id, name, data, levels):
        self.id = id
        self.name = name
        self.data = data
        self.levels = levels

    
    def __repr__(self) -> str:
        return f'<AppSection(id={self.id}, name={self.name}, data={self.data}, levels={self.levels})>'


    def __str__(self) -> str:
        return f'<AppSection(id={self.id}, name={self.name}, data={self.data}, levels={self.levels})>'


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
    levels = []

    def __init__(self, iduser, apps=None, levels=None):

        self.iduser = iduser
        if apps:
            self.app = self.app.append(apps)
        else:
            self.app = []

        if levels:
            self.levels = self.levels.append(levels)
        else:
            self.levels = []


    def __str__(self) -> str:
        return f'<Autorization(iduser={self.iduser}, app={self.app})>'

    
    def add_app(self, app):
        self.app.append(app)


    def update_app(self, abstapp):
        
        for i in range(len(self.app)):
            if abstapp.id == self.app[i].id:
                self.app[i].add_section(abstapp.section[0])
                return

        self.app.append(abstapp)

        return
    


    @staticmethod
    def get_by_id_user(iduser):

        obj_autorization = Autorization(iduser)
        ls_obj_access = Access.simple_filter(user_iduser=iduser)

        for obj_access in ls_obj_access:

            obj_app_section = AppSection.get_by_id(obj_access.app_section_idapp_section)
            obj_abstr_app_section = AbstractAppSection(obj_app_section.idapp_section, obj_app_section.name, obj_app_section.data, obj_access.get_levels())
            obj_app = App.get_by_id(obj_app_section.app_idapp)
            obj_abstr_app = AbstractApp(obj_app.idapp, obj_app.name, obj_abstr_app_section)
            obj_autorization.update_app(obj_abstr_app)

        """
        for obj_access in ls_obj_access:
            print(f'obj_access: {obj_access}')
            for idlevel in obj_access.level:
                print(f'idlevel: {idlevel}')
                obj_level = Level.get_by_id(idlevel)
                print(f'niveles desde levels_by_id: {obj_level}')

            print(f'niveles desde access: {obj_access.get_levels()}')
        """
        return obj_autorization
    