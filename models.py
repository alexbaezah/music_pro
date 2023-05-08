from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Region(db.Model):
    __tablename__ = 'REGION'
    id_region = db.Column(db.Integer, primary_key=True)
    nombre_reg = db.Column(db.String(80), nullable=False)
    
    ciudades = db.relationship('Ciudad', backref='region', lazy=True)

class Ciudad(db.Model):
    __tablename__ = 'CIUDAD'
    id_ciudad = db.Column(db.Integer, primary_key=True)
    nom_ciud = db.Column(db.String(80), nullable=False)
    id_region = db.Column(db.Integer, db.ForeignKey('REGION.id_region'), nullable=False)

    comunas = db.relationship('Comuna', backref='ciudad', lazy=True)

class Comuna(db.Model):
    __tablename__ = 'COMUNA'
    id_com = db.Column(db.Integer, primary_key=True)
    nom_com = db.Column(db.String(100), nullable=False)
    id_ciudad = db.Column(db.Integer, db.ForeignKey('CIUDAD.id_ciudad'), nullable=False)
    id_region = db.Column(db.Integer, db.ForeignKey('REGION.id_region'), nullable=False)