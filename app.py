from flask import Flask, render_template
from templates.db_model.Commentaire import db
from crud.commentaire import methods

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://uuizwvipdgu54gkvrgih:m2YRt73v9SpJzn8YraGh@bzlztrcmulrukkyuyijd-postgresql.services.clever-cloud.com:5432/bzlztrcmulrukkyuyijd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def home():
    return render_template('html/home.html')


@app.route('/api/quentin/commentaires', methods=['POST'])
def create_commentaire():
    return methods.create_commentaire()


@app.route('/api/quentin/commentaires', methods=['GET'])
def index():
    return methods.index()


@app.route('/api/quentin/commentaire/<id>', methods=['GET'])
def get_commentaire_by_id(id):
    return methods.get_commentaire_by_id(id)


@app.route('/api/quentin/commentaire/<id>', methods=['PUT'])
def update_commentaire_by_id(id):
    return methods.update_commentaire_by_id(id)


@app.route('/api/quentin/commentaire/<id>', methods=['DELETE'])
def delete_commentaire_by_id(id):
    return methods.delete_commentaire_by_id(id)


if __name__ == '__main__':
    app.run()
