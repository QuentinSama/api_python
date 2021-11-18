from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

db = SQLAlchemy()

class Personne(db.Model):
    __tablename__ = "Personne"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    mail = db.Column(db.String(50))
    numTel = db.Column(db.String(50))
    sexe = db.Column(db.String(50))


class PersonneSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Personne
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    nom = fields.String(required=True)
    prenom = fields.String(required=True)
    mail = fields.String(required=True)
    numTel = fields.String(required=True)
    sexe = fields.String(required=True)
