import requests
import os
from dotenv import load_dotenv

load_dotenv()

WASSENGER_API_KEY = os.getenv("WASSENGER_API_KEY")
WASSENGER_DEVICE_ID = os.getenv("WASSENGER_DEVICE_ID")
WASSENGER_BASE_URL = "https://api.wassenger.com/v1"

def envoyer_message(numero, message):
    url = f"{WASSENGER_BASE_URL}/messages"
    headers = {
        "Token": WASSENGER_API_KEY,
        "Content-Type": "application/json"
}
    payload = {
        "phone": numero,
        "message": message,
        "device": WASSENGER_DEVICE_ID
}

    try:
        response = requests.post(url, json=payload, headers=headers)
        return response.status_code == 200
    except Exception as e:
        print(f"Erreur envoi WhatsApp: {e}")
        return False