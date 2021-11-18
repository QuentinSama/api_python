from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

db = SQLAlchemy()

class Commentaire(db.Model):
    __tablename__ = "Commentaire"
    id = db.Column(db.Integer, primary_key=True)
    corps = db.Column(db.String(255))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, corps):
        self.corps = corps

    def __repr__(self):
        return f"{self.id}"



class CommentaireSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Commentaire
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    corps = fields.String(required=True)