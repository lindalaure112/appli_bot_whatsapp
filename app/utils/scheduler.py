from apscheduler.schedulers.background import BackgroundScheduler
from app import db
from app.models import ScheduledMessage
from app.utils.whatsapp_api import envoyer_message
from datetime import datetime
import pytz

scheduler = BackgroundScheduler()

def verifier_et_envoyer():
    now = datetime.utcnow()
    messages = ScheduledMessage.query.filter_by(statut='en_attente').all()

    for msg in messages:
        # Convertir l’heure planifiée au bon fuseau horaire
        tz = pytz.timezone(msg.fuseau_horaire)
        heure_locale = tz.localize(msg.date_heure).astimezone(pytz.utc)

        if heure_locale <= now:
            success = envoyer_message(msg.groupe, msg.contenu)
            msg.statut = 'envoyé' if success else 'échoué'
            db.session.commit()

def demarrer_planificateur():
    scheduler.add_job(func=verifier_et_envoyer, trigger="interval", seconds=60)
    scheduler.start()