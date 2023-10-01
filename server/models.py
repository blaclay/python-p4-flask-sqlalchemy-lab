from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    birthday = db.Column(db.String, unique=True)

    # animals = db.Column(db.String, db.ForeignKey('animals.name'))
    animals = db.relationship('Animal', backref='zookeeper')

    # Zookeeper = db.relationship('Zookeeper', backref='zookeeper')

    # def __repr__(self):
    #     return f'<Zookeeper {self.name}>'

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)

    # enclosure = db.Column(db.String, unique=True)
    # Enclosure = db.relationship('Enclosure', backref='enclosure')
    # "open_to_visitors" boolean
    open_to_visitors = db.Column(db.Boolean)
    animals = db.relationship('Animal', backref='enclosure')

    # def __repr__(self):
    #     return f'<Enclosure {self.environment}>'

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    species = db.Column(db.String, unique=True)

    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))
    # zookeeper_name = db.Column(db.String, db.ForeignKey('zookeepers.name'))
    # enclosure_environment = db.Column(db.String, db.ForeignKey('enclosures.environment'))
