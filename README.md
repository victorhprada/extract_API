# Bitcoin Price Monitor

Sistema de monitoramento do preço do Bitcoin em tempo real, com ETL automatizado e dashboard interativo.

## Estrutura do Projeto

```
.
├── src/
│   ├── pipeline_03.py      # ETL com PostgreSQL
│   ├── pipeline_04.py      # ETL com logging avançado
│   ├── database.py         # Modelo do banco de dados
│   └── requirements.txt    # Dependências do ETL
├── app/
│   ├── dashboard_00.py     # Dashboard demo com elementos Streamlit
│   ├── dashboard_01.py     # Dashboard do Bitcoin em tempo real
│   └── requirements.txt    # Dependências do dashboard
└── .env                    # Variáveis de ambiente
```

## Funcionalidades

### ETL (src/)
- Coleta de dados da API Coinbase
- Transformação e normalização dos dados
- Armazenamento em PostgreSQL
- Sistema de logging com Logfire
- Execução automática a cada 15 segundos

### Dashboard (app/)
- Visualização em tempo real do preço do Bitcoin
- Gráfico histórico de preços
- Estatísticas (preço atual, máximo e mínimo)
- Interface interativa com Streamlit

## Configuração

1. Instale as dependências:
```bash
# Para o ETL
cd src/
pip install -r requirements.txt

# Para o dashboard
cd app/
pip install -r requirements.txt
```

2. Configure as variáveis de ambiente no arquivo `.env`:
```
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_DB=nome_do_banco
POSTGRES_HOST=host_do_banco
POSTGRES_PORT=5432
LOGFIRE_TOKEN=seu_token_logfire
```

## Execução

1. Inicie o ETL:
```bash
python src/pipeline_04.py
```

2. Inicie o dashboard:
```bash
streamlit run app/dashboard_01.py
```

## Tecnologias Utilizadas

- Python
- PostgreSQL
- SQLAlchemy
- Streamlit
- Logfire
- Pandas
- Requests
