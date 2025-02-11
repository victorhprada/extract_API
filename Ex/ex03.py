import requests
import json

url3 = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'

headers = {
    'Accept': 'application/json',
    'User-Agent': 'MinhaAplicacao/1.0'
}

params = {'currency': 'USD'}

try:
    response = requests.get(url3, headers=headers, params=params)
    response.raise_for_status()  # Verifica se houve erro na requisição
    
    print("Status Code:", response.status_code)
    print("Response Text:", response.text[:200])  # Primeiros 200 caracteres da resposta
    
    data = response.json()
    print(f"Preço do Bitcoin: {data['data']['amount']}")
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON: {e}")
    print("Resposta completa:", response.text)