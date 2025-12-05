
from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

#UTILISATEURS
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mot_de_passe_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default='utilisateur')  # ou 'admin'
    date_inscription = db.Column(db.DateTime, default=datetime.utcnow)

    programmations = db.relationship('ScheduledMessage', backref='utilisateur', lazy=True)

    def set_password(self, mot_de_passe):
        self.mot_de_passe_hash = generate_password_hash(mot_de_passe)

    def check_password(self, mot_de_passe):
        return check_password_hash(self.mot_de_passe_hash, mot_de_passe)
    
    #PROMMATIONS DE COURS OU MESSAGES
    class ScheduledMessage(db.Model):
     id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    contenu = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(20), default='texte')  # texte, image, vidéo, audio
    groupe = db.Column(db.String(100), nullable=False)
    date_heure = db.Column(db.DateTime, nullable=False)
    fuseau_horaire = db.Column(db.String(50), default='Africa/Douala')
    statut = db.Column(db.String(20), default='en_attente')  # en_attente, envoyé, échoué

#COURS INFORMATIQUES
    class Course(db.Model):
     id = db.Column(db.Integer, primary_key=True)
    sujet = db.Column(db.String(100), nullable=False)  # architecture, OS, réseaux
    niveau = db.Column(db.String(50), default='débutant')
    type = db.Column(db.String(20), default='texte')  # texte, pdf, vidéo
    contenu = db.Column(db.Text, nullable=True)
    lien = db.Column(db.String(255), nullable=True)

#JEUX INTERACTIFS
    class GameSession(db.Model):
     id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    type = db.Column(db.String(50))  # quiz, devinette, etc.
    score = db.Column(db.Integer, default=0)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    #MEDIAS recus ou envoyes
    class MediaLog(db.Model):
     id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    type = db.Column(db.String(20))  # image, vidéo, audio, document
    url = db.Column(db.String(255))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    #Bonus de connection (200 Mo)
    class ConnectionBonus(db.Model):
     id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_connexion = db.Column(db.DateTime, default=datetime.utcnow)
    bonus_offert = db.Column(db.Boolean, default=False)