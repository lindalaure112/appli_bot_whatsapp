
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.utils.whatsapp_api import envoyer_message

bp = Blueprint('messaging', __name__, url_prefix='/messaging')

@bp.route('/test', methods=['GET'])
@jwt_required()
def test_envoi():
    success = envoyer_message("NuméroTest", "Message test depuis le bot")
    return jsonify(status="envoyé" if success else "échec")