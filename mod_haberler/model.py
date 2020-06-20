from app import db

class Haberler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    haberKodu = db.Column(db.String(30))
    haberTuru = db.Column(db.String(50))
    haberIcerik = db.Column(db.String(255))