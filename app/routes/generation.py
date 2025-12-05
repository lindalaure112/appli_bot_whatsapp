
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.utils.replicate_api import generer_image

bp = Blueprint('generation', __name__, url_prefix='/generation')

@bp.route('/image', methods=['POST'])
@jwt_required()
def image():
    data = request.get_json()
    prompt = data['prompt']
    url = generer_image(prompt)
    return jsonify(image_url=url)