from app.db import db, BaseModelMixin

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