
from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from flask_jwt_extended import create_access_token

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(nom=data['nom'], email=data['email'])
    user.set_password(data['mot_de_passe'])
    db.session.add(user)
    db.session.commit()
    return jsonify(message="Utilisateur enregistré avec succès"), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['mot_de_passe']):
        token = create_access_token(identity=user.id)
        return jsonify(token=token), 200
    return jsonify(message="Identifiants invalides"), 401