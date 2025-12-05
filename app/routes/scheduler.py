
from flask import Blueprint, request, jsonify
from app import db
from app.models import ScheduledMessage
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('scheduler', __name__, url_prefix='/scheduler')

@bp.route('/planifier', methods=['POST'])
@jwt_required()
def planifier():
    data = request.get_json()
    user_id = get_jwt_identity()
    message = ScheduledMessage(
        user_id=user_id,
        contenu=data['contenu'],
        type=data.get('type', 'texte'),
        groupe=data['groupe'],
        date_heure=datetime.fromisoformat(data['date_heure']),
        fuseau_horaire=data.get('fuseau_horaire', 'Africa/Douala')
)
    db.session.add(message)
    db.session.commit()
    return jsonify(message="Message programmé avec succès"), 201