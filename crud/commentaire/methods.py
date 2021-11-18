from flask import Flask, request, jsonify, make_response
from templates.db_model.Commentaire import CommentaireSchema, Commentaire, db



def create_commentaire():
    data = request.get_json()
    commentaire_schema = CommentaireSchema()
    commentaire = commentaire_schema.load(data)
    result = commentaire_schema.dump(commentaire.create())
    return make_response(jsonify({"commentaire": result}), 200)


def index():
    get_commentaire = Commentaire.query.all()
    commentaire_schema = CommentaireSchema(many=True)
    commentaires = commentaire_schema.dump(get_commentaire)
    return make_response(jsonify({"commentaires": commentaires}))


def get_commentaire_by_id(id):
    get_commentaire = Commentaire.query.get(id)
    commentaire_schema = CommentaireSchema()
    commentaire = commentaire_schema.dump(get_commentaire)
    return make_response(jsonify({"commentaire": commentaire}))


def update_commentaire_by_id(id):
    data = request.get_json()
    get_commentaire = Commentaire.query.get(id)
    if data.get('corps'):
        get_commentaire.corps = data['corps']
    db.session.add(get_commentaire)
    db.session.commit()
    commentaire_schema = CommentaireSchema(only=['id', 'corps'])
    commentaire = commentaire_schema.dump(get_commentaire)

    return make_response(jsonify({"commentaire": commentaire}))


def delete_commentaire_by_id(id):
    get_commentaire = Commentaire.query.get(id)
    db.session.delete(get_commentaire)
    db.session.commit()
    return make_response("DELETE OK", 204)
