
from flask import Blueprint, jsonify
from app.models import Course

bp = Blueprint('courses', __name__, url_prefix='/courses')

@bp.route('/liste', methods=['GET'])
def liste():
    cours = Course.query.all()
    return jsonify([{
        'id': c.id,
        'sujet': c.sujet,
        'niveau': c.niveau,
        'type': c.type,
        'contenu': c.contenu,
        'lien': c.lien
} for c in cours])