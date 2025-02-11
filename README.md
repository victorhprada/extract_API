
# API Integration Examples

Este repositório contém exemplos de integração com diferentes APIs usando Python.

## Estrutura do Projeto

- `Ex/ex01.py`: Exemplos básicos de requisições HTTP
  - Integração com API do GitHub (eventos)
  - Requisição simples ao Google

- `Ex/ex02.py`: Exemplo de API com parâmetros
  - Integração com JSONPlaceholder
  - Demonstração de filtragem de comentários por postId

- `Ex/ex03.py`: Integração com Coinbase API
  - Consulta preço do Bitcoin em tempo real
  - Tratamento de erros na requisição
  - Headers personalizados

- `Ex/ex04.py`: Integração com OpenAI API
  - Exemplo de chat completion com GPT-3.5
  - Uso de variáveis de ambiente para chaves de API
  - Tratamento de erros e limites de quota

## Configuração

1. Instale as dependências:
```bash
pip install requests python-dotenv
```

2. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione sua chave da OpenAI:
```
chave=sua_chave_da_openai_aqui
```

## Observações

- Certifique-se de ter uma chave válida da OpenAI para o ex04.py
- As requisições incluem tratamento de erros básico
- Alguns exemplos incluem headers personalizados para melhor interação com as APIs
