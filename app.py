from flask import Flask, request, jsonify, make_response, render_template
from templates.db_model.Personne import Personne, PersonneSchema, db
from crud.personne import methods

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://uuizwvipdgu54gkvrgih:m2YRt73v9SpJzn8YraGh@bzlztrcmulrukkyuyijd-postgresql.services.clever-cloud.com:5432/bzlztrcmulrukkyuyijd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)
with app.app_context():
    db.create_all()


    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


    def __init__(self, nom, prenom, mail, numTel, sexe):
        self.nom = nom
        self.prenom = prenom
        self.mail = mail
        self.numTel = numTel
        self.sexe = sexe


    def __repr__(self):
        return f"{self.id}"


@app.route('/', methods=['GET'])
def home():
    return render_template('html/home.html')


@app.route('/api/quentin/personne', methods=['POST'])
def create_personne():
    return methods.create_personne()


@app.route('/api/quentin/personnes', methods=['GET'])
def index():
    return methods.index()


@app.route('/api/quentin/personne/<id>', methods=['GET'])
def get_personne_by_id(id):
    return methods.get_personne_by_id(id)


@app.route('/api/quentin/personne/<id>', methods=['PUT'])
def update_personne_by_id(id):
    return methods.update_personne_by_id(id)


@app.route('/api/quentin/personne/<id>', methods=['DELETE'])
def delete_personne_by_id(id):
    return methods.delete_personne_by_id(id)


if __name__ == '__main__':
    app.run()
