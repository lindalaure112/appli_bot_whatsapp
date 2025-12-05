from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

bp = Blueprint('games', 'name', url_prefix='/games')

@bp.route('/quiz', methods=['GET'])
@jwt_required()
def quiz():
    question = {
        "question": "Quel est le rôle du BIOS?",
        "options": ["Gérer la mémoire", "Démarrer le système", "Afficher l’écran", "Contrôler le clavier"],
        "réponse": "Démarrer le système"
}
    return jsonify(question)