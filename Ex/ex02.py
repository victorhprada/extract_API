import requests

url3 = 'https://jsonplaceholder.typicode.com/comments'

params = {'postId': 1} # Obtendo apenas comentários do post com ID 1

response3 = requests.get(url3, params=params)

comentarios = response3.json()
print(f"Foram encontrados {len(comentarios)} comentários")
print(f"Erro: {response3.status_code} - {response3.text}")