from flask import Blueprint

# Initialisation des blueprints
bp = Blueprint('routes', __name__)

from app.routes import auth, scheduler, messaging, media, generation, courses, games