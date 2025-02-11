import os
import time
import requests
from datetime import datetime
from sqlalchemy import create_engine # Criando o motor do banco de dados
from sqlalchemy.orm import sessionmaker # Criando o sessionmaker
from database import Base, Bitcoin # Importando a classe Bitcoin
from dotenv import load_dotenv  # Carregando as variáveis de ambiente

load_dotenv() # Carregando as variáveis de ambiente

# Pegando as variáveis de ambiente
POSTGRES_USER=os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB=os.getenv('POSTGRES_DB')
POSTGRES_HOST=os.getenv('POSTGRES_HOST')
POSTGRES_PORT=os.getenv('POSTGRES_PORT')

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Criando a engine e sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def create_table():
    # Criando a tabela no banco de dados, se não existir
    Base.metadata.create_all(bind=engine)
    print('Tabela criada/verificada com sucesso')

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

def save_postgres_data(dados):
    # Salvar os dados no banco de dados PostgreSQL
    session = Session() # Criando a sessão
    new_registration = Bitcoin(**dados) # Criando o novo registro
    session.add(new_registration) # Adicionando o novo registro à sessão
    session.commit() # Salvando o novo registro
    session.close() # Fechando a sessão
    print(f'[{dados["timestamp"]}] Dados salvos no banco de dados PostgreSQL com sucesso')

# print(transform_data_bitcoin(extract_data_bitcoin()))

if __name__ == '__main__':
    create_table()
    print('Iniciando ETL com atualização de dados a cada 15 segundos (CTRL + C para interromper)')
    while True:
        try:
            dados_json = extract_data_bitcoin()
            if dados_json:
                dados_tratados = transform_data_bitcoin(dados_json) # Transformando os dados
                print(f'Dados tratados com sucesso, {dados_tratados}')
                save_postgres_data(dados_tratados) # Salvando os dados no banco de dados
                time.sleep(15)
        except Exception as e:
            print(f'Erro: {e}')
            time.sleep(15)
    
    