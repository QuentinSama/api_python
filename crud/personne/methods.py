from flask import Flask, request, jsonify, make_response
from templates.db_model.Personne import PersonneSchema, Personne
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_personne():
    data = request.get_json()
    personne_schema = PersonneSchema()
    personne = personne_schema.load(data)
    result = personne_schema.dump(personne.create())
    return make_response(jsonify({"Personne": result}), 200)


def index():
    get_personne = Personne.query.all()
    personne_schema = PersonneSchema(many=True)
    personnes = personne_schema.dump(get_personne)
    return make_response(jsonify({"Personnes": personnes}))


def get_personne_by_id(id):
    get_personne = Personne.query.get(id)
    personne_schema = PersonneSchema()
    personne = personne_schema.dump(get_personne)
    return make_response(jsonify({"personne": personne}))


def update_personne_by_id(id):
    data = request.get_json()
    get_personne = Personne.query.get(id)
    if data.get('nom'):
        get_personne.nom = data['nom']
    if data.get('prenom'):
        get_personne.prenom = data['prenom']
    if data.get('mail'):
        get_personne.mail = data['mail']
    if data.get('numTel'):
        get_personne.numTel = data['numTel']
    if data.get('sexe'):
        get_personne.sexe = data['sexe']
    db.session.add(get_personne)
    db.session.commit()
    personne_schema = PersonneSchema(only=['id', 'nom', 'prenom', 'mail', 'numTel', 'sexe'])
    personne = personne_schema.dump(get_personne)

    return make_response(jsonify({"Personne": personne}))


def delete_personne_by_id(id):
    get_personne = Personne.query.get(id)
    db.session.delete(get_personne)
    db.session.commit()
    return make_response("DELETE OK", 204)
