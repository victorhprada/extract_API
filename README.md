# ETL Project with Python Requests

## Descrição
Projeto de ETL (Extract, Transform, Load) desenvolvido em Python utilizando a biblioteca Requests para extrair dados de APIs REST, realizar transformações e carregar em um destino.

## Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)

## Bibliotecas Principais
- requests
- pandas
- python-dotenv
- logging

## Instalação
1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/nome-do-projeto.git
cd nome-do-projeto
```

2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
API_KEY=sua_chave_api
API_URL=https://api.exemplo.com/v1
```

## Uso
Execute o script principal:
```bash
python main.py
```

## 📁 Estrutura do Projeto
```
projeto/
├── src/
│   ├── extract.py    # Funções de extração
│   ├── transform.py  # Funções de transformação
│   └── load.py       # Funções de carregamento
├── data/            # Dados brutos e processados
├── logs/            # Arquivos de log
├── .env            # Variáveis de ambiente
├── requirements.txt # Dependências
└── main.py         # Script principal
```
