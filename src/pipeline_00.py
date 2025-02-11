import requests
from tinydb import TinyDB
from datetime import datetime

def extract_data_bitcoin():
    url = 'https://api.coinbase.com/v2/prices/spot'

    response = requests.get(url)
    dados = response.json()

    return dados

# print(extract_data_bitcoin()['data'])

def transform_data_bitcoin(dados): # Tranformando os dados para o formato desejado
    valor = dados['data']['amount']
    cripto = dados['data']['base']
    moeda = dados['data']['currency']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    transform_data = {
        'valor': valor,
        'cripto': cripto,
        'moeda': moeda,
        'timestamp': timestamp
    }

    return transform_data

def save_tinydb_data(dados, db_name='bitcoin.json'):
    db = TinyDB(db_name)
    db.insert(dados)
    print(f'Dados salvos em {db_name}')

# print(transform_data_bitcoin(extract_data_bitcoin()))

if __name__ == '__main__':
    # Extraindo os dados
    dados_json = extract_data_bitcoin()
    dados_transformados = transform_data_bitcoin(dados_json)
    save_tinydb_data(dados_transformados)
    