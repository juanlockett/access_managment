from app.db import db, BaseModelMixin

class App(db.Model, BaseModelMixin):
    __tablename__ = 'app'

    idapp = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))

    section = db.relationship('AppSection', back_populates='app', lazy=False, cascade='all, delete-orphan')


    def __init__(self, name, apikey):
        self.name = name
        self.apikey = apikey

    
    def __repr__(self):
        return f'<App(name={self.name})>'

    
    def __str__(self):
        return f'{self.name}'



class AppSection(db.Model, BaseModelMixin):
    __tablename__ = 'app_section'

    idapp_section = db.Column(db.Integer, primary_key=True)
    app_idapp = db.Column(db.ForeignKey('app.idapp'), nullable=False, index=True)
    name = db.Column(db.String(45))
    data = db.Column(db.String(45))

    app = db.relationship('App')


    def __init__(self, name, data):
        self.name = name
        self.data = data


    def __repr__(self):
        return f'<AppSection(name={self.name})>'


    def __str__(self):
        return f'{self.name}'