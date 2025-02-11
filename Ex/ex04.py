import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url4 = 'https://api.openai.com/v1/chat/completions'

openai_api_key = os.getenv("chave")

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {openai_api_key}'  # Substitua com sua nova chave
}

data = {
    'model': 'gpt-3.5-turbo',
    'messages': [{'role': 'user', 'content': 'Qual a capital do Brasil?'}]
}

try:
    response = requests.post(url4, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")
    if response.status_code == 429:
        print("Erro de quota excedida. Verifique seu plano e saldo.")