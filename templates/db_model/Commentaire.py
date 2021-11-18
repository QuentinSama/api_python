from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

db = SQLAlchemy()

class Commentaire(db.Model):
    __tablename__ = "Commentaire"
    id = db.Column(db.Integer, primary_key=True)
    corps = db.Column(db.String(255))


class CommentaireSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Commentaire
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    corps = fields.String(required=True)