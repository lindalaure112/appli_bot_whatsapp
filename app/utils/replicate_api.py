import requests
import os
from dotenv import load_dotenv

load_dotenv()

REPLICATE_API_KEY = os.getenv("REPLICATE_API_KEY")
REPLICATE_MODEL = "stability-ai/stable-diffusion"  # ou un autre modèle

def generer_image(prompt):
    url = "https://api.replicate.com/v1/predictions"
    headers = {
        "Authorization": f"Token {REPLICATE_API_KEY}",
        "Content-Type": "application/json"
}
    data = {
        "version": "db21e45e...",  # Remplace par la version exacte du modèle
        "input": {
            "prompt": prompt
}
}

    try:
        response = requests.post(url, json=data, headers=headers)
        result = response.json()
        return result.get("urls", {}).get("get")  # URL de l’image générée
    except Exception as e:
        print(f"Erreur Replicate: {e}")
        return None