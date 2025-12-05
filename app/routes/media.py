
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

bp = Blueprint('media', __name__, url_prefix='/media')

@bp.route('/reception', methods=['POST'])
@jwt_required()
def recevoir_media():
    # À implémenter: traitement des médias entrants
    return jsonify(message="Réception de média en cours")