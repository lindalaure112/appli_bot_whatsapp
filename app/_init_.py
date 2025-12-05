from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    jwt.init_app(app)

    from app.routes import auth, scheduler, messaging, media, generation, courses, games
    app.register_blueprint(auth.bp)
    app.register_blueprint(scheduler.bp)
    app.register_blueprint(messaging.bp)
    app.register_blueprint(media.bp)
    app.register_blueprint(generation.bp)
    app.register_blueprint(courses.bp)
    app.register_blueprint(games.bp)

    return app